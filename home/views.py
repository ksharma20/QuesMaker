from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from editor.models import QuestionPapers, Question

# Create your views here.
def index(request):
    if request.method == 'POST':
        pass

    if request.user.is_authenticated:
        Quespapers = QuestionPapers.objects.all()
        return render(request, 'index.html', {'uname': request.user.username, 'Message': 'Welcome to QuizMakers' ,'QuesPaper': Quespapers })
    else:
        return redirect('/login')

    
    
def ulogin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passw = request.POST.get('passw')
        user = authenticate(username=uname, password=passw)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def ulogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
    else:
        return redirect('/')

