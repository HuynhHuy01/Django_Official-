# Generated by Django 4.2.1 on 2023-05-18 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_bookstoread_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcardsmodel',
            name='book_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
