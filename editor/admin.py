from django.contrib import admin
from .models import Question, QuestionPapers

# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionPapers)