# Generated by Django 2.1.7 on 2019-08-10 10:17

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('library', '0004_auto_20190809_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='keywords',
        ),
        migrations.AddField(
            model_name='code',
            name='keywords',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]