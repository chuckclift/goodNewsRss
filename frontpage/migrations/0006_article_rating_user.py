# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0005_article_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_rating',
            name='user',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
