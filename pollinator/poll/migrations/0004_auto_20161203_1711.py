# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 23:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20161123_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='answer_text',
        ),
    ]
