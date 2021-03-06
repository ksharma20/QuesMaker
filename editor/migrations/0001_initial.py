# Generated by Django 3.2.9 on 2021-12-01 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPapers',
            fields=[
                ('qpid', models.AutoField(primary_key=True, serialize=False)),
                ('qpno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('qno', models.IntegerField()),
                ('set_name', models.CharField(max_length=1)),
                ('marks', models.IntegerField()),
                ('qtext', models.TextField()),
                ('qimg', models.ImageField(upload_to='')),
                ('qpid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.questionpapers')),
            ],
        ),
    ]
