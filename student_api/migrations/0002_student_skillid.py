# Generated by Django 5.1.4 on 2025-01-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='skillId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
