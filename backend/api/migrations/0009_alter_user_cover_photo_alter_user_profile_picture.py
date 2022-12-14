# Generated by Django 4.1 on 2022-09-29 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_user_cover_photo_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cover_photo',
            field=models.ImageField(blank=True, default='/media/cover_photo/default.jpeg', upload_to='media/cover_photo/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='/media/profile_picture/default.jpg', upload_to='media/profile_picture/%Y/%m/%d'),
        ),
    ]
