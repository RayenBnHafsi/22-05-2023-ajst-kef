# Generated by Django 4.2 on 2023-04-27 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AJSK_RH', '0003_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_file',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]