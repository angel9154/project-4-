# Generated by Django 5.1.4 on 2025-01-10 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skill_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='skill_api.skill')),
            ],
        ),
    ]
