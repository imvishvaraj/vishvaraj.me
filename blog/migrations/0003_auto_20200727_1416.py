# Generated by Django 3.0.3 on 2020-07-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200725_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='first_img',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='posts_imgs/%y/'),
        ),
        migrations.AddField(
            model_name='post',
            name='first_img_caption',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
