# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 22:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20161123_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_date',
            new_name='pub_date',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_name',
            new_name='question_text',
        ),
    ]
