# Generated by Django 5.0.6 on 2024-12-04 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_post_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='init_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('body', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('banner', models.ImageField(blank=True, default='image.png', upload_to='')),
            ],
        ),
    ]
