# Generated by Django 4.1 on 2022-10-11 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_remove_comments_retweetid_remove_media_retweetid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_quoteId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_quote', to='api.comments'),
        ),
    ]
