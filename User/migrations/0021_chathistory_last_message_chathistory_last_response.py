# Generated by Django 5.0.6 on 2024-11-14 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0020_remove_chatmessage_user_chathistory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chathistory',
            name='last_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chathistory',
            name='last_response',
            field=models.TextField(blank=True, null=True),
        ),
    ]