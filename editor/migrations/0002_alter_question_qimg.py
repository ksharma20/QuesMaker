# Generated by Django 3.2.9 on 2021-12-02 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qimg',
            field=models.ImageField(blank=True, upload_to='static/'),
        ),
    ]
