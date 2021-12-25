from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import QuestionPapers,Question
from .forms import QuespaperForm, QuesForm

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        subject = request.POST.get('subject')
        num = request.POST.get('num')
        img = request.FILES.get('img')
        oj = QuestionPapers.objects.get_or_create(subject = subject, num = num, img = img)
 
        return redirect(f'/edit/{oj[0].id}/ques')
    
    return render(request, 'qpedit.html')
   

def qadd(request, id):
    obj = QuestionPapers.objects.get(id =id)
    if request.method == 'POST':
        form = QuesForm(request.POST, request.FILES)
        if form.is_valid():
            Question.objects.get_or_create(set_name = form.cleaned_data['set_name'], num = form.cleaned_data['num'], img = form.cleaned_data['img'], marks = form.cleaned_data['marks'], text = form.cleaned_data['text'], qpid = QuestionPapers.objects.get(id = id))
            return redirect(f'/edit/{obj.id}/ques')
        else:
            return render(request, 'qedit.html' , {'form': form, 'QP': obj})
    
    else:
        form = QuesForm()
    
    return render(request, 'qedit.html' , {'form': form, 'QP': obj})

def qedit(request, id):
    obj = Question.objects.get(id=id)
    form = QuesForm(instance=obj)
    if request.method == 'POST':
        form = QuesForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            obj.num = form.cleaned_data['num']
            obj.set_name = form.cleaned_data['set_name']
            obj.marks = form.cleaned_data['marks']
            obj.text  = form.cleaned_data['text']
            obj.img = form.cleaned_data['img']
            obj.save()
            return redirect(f'/edit/{obj.qpid.id}/ques')
        else:
            return render(request, 'qedit.html' , {'form': form, 'QP': obj.qpid})
    

    return render(request, 'qedit.html' , {'form': form, 'QP': obj.qpid})


def qpedit(request, id):
    try:
        obj = QuestionPapers.objects.get(id=id)
    except:
        return HttpResponse("ID is wrong")
    
    if request.method == 'POST':
        try:
            obj.subject = request.POST.get('subject')
            obj.num = request.POST.get('num')
            obj.img = request.FILES.get('img')
            obj.save()
        except:
            pass
        return redirect('/')
    
    return render(request, 'qpedit.html', {'Qid': obj})


def qpshow(request, id):
    context = {
        'Ques': Question.objects.filter(qpid = id),
        'SETA': Question.objects.filter(qpid = id, set_name = 'A'),
        'SETB': Question.objects.filter(qpid = id, set_name = 'B'),
        'SETC': Question.objects.filter(qpid = id, set_name = 'C'),
        'SETD': Question.objects.filter(qpid = id, set_name = 'D'),
        'Qp': QuestionPapers.objects.get(id =id),
        }
    return render(request, 'qpques.html', context)


def qpdel(request, id):
    try:
        obj = QuestionPapers.objects.get(id=id)
    except:
        return HttpResponse("ID is wrong")
    
    obj.delete()
    return redirect('/')


def qdel(request, id):
    try:
        obj = Question.objects.get(id=id)
    except:
        return HttpResponse("ID is wrong")
    qid = obj.qpid.id
    obj.delete()
    return redirect(f'/edit/qp/{qid}/ques')