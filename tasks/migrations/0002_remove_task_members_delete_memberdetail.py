# Generated by Django 5.0.4 on 2024-04-07 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='members',
        ),
        migrations.DeleteModel(
            name='MemberDetail',
        ),
    ]
