# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-19 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0002_article_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.IntegerField(default=0)),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='score',
        ),
        migrations.AddField(
            model_name='article',
            name='source_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.CharField(default='https://www.researchnews.com/rss.xml', max_length=300),
            preserve_default=False,
        ),
    ]
