# Generated by Django 4.2.5 on 2024-01-06 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_alter_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('館藏中', 'available'), ('外借中', 'borrowed')], default='館藏中', max_length=20),
        ),
    ]
