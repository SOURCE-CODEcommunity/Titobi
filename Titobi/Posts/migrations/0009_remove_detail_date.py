# Generated by Django 5.1.3 on 2024-12-05 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0008_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='date',
        ),
    ]
