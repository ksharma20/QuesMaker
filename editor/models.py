from django.db import models

# Create your models here.
class QuestionPapers(models.Model):

    id = models.AutoField(primary_key=True)
    img = models.ImageField(blank=True, upload_to='static/quespaper/')
    num = models.IntegerField()
    subject = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.num} '+ self.subject


class Question(models.Model):

    id = models.AutoField(primary_key=True)
    num = models.IntegerField()
    set_name = models.CharField(max_length=1, choices=[('A', 'A'),('B', 'B'),('C', 'C'),('D', 'D')], default='A')
    marks = models.IntegerField()
    text = models.TextField()
    img = models.ImageField(blank=True, upload_to='static/ques/')
    qpid = models.ForeignKey(QuestionPapers, on_delete= models.CASCADE, related_name='Qpaper')

    def __str__(self):
        return self.text[:25]


# Flushing primary key from DataBase where table Name= appname_modelname
# DELETE FROM your_table; DELETE FROM SQLite_sequence WHERE name='your_table';