# Generated by Django 2.1.4 on 2019-08-09 17:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20190807_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code',
            field=tinymce.models.HTMLField(),
        ),
    ]