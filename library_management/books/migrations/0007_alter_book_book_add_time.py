# Generated by Django 5.0.1 on 2024-01-31 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_book_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_add_time',
            field=models.TimeField(default=datetime.datetime(2024, 1, 31, 20, 32, 37, 861334, tzinfo=datetime.timezone.utc)),
        ),
    ]
