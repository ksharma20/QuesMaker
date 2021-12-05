from django import forms
from editor.models import Question, QuestionPapers


class QuespaperForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Subject Name ')
    num = forms.IntegerField(label='Question Paper Number ')
    img = forms.ImageField(label='Thumbnail Image ')

class QuesForm(forms.ModelForm):
    class Meta:
       model = Question
       fields = ['num', 'set_name', 'marks', 'text', 'img']
    # num = forms.IntegerField(label='Question Number ')
    # set_name = forms.ChoiceField(label='Set Name ', choices=[('A', 'A'),('B', 'B'),('C', 'C'),('D', 'D')], required=True)
    # marks = forms.IntegerField(label='Marks ')
    # text = forms.CharField(widget=forms.Textarea, label='Question Text ')
    # img = forms.ImageField(label='Image for your Ques')
    # qpid = forms.ModelChoiceField(QuestionPapers.objects.all())
