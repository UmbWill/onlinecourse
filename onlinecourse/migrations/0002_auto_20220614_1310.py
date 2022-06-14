# Generated by Django 3.1.3 on 2022-06-14 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='questions',
        ),
        migrations.AddField(
            model_name='choice',
            name='questions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
        ),
        migrations.RemoveField(
            model_name='question',
            name='lessons',
        ),
        migrations.AddField(
            model_name='question',
            name='lessons',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'),
        ),
    ]
