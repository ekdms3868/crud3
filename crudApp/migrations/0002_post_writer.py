# Generated by Django 3.2.3 on 2021-05-24 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.CharField(default='some_value', max_length=15),
        ),
    ]
