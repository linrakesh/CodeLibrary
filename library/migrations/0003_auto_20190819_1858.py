# Generated by Django 2.1.4 on 2019-08-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_code_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='updated_on',
            field=models.DateField(auto_now=True),
        ),
    ]
