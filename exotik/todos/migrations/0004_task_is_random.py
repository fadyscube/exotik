# Generated by Django 4.0.3 on 2022-04-08 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_task_user_alter_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_random',
            field=models.BooleanField(default=False),
        ),
    ]
