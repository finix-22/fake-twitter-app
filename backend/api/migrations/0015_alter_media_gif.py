# Generated by Django 4.1 on 2022-10-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_media_gif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='gif',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
