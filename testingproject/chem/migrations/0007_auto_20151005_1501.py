# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chem', '0006_userprofile_counter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='counter',
            new_name='count',
        ),
    ]
