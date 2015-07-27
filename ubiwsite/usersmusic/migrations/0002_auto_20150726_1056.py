# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersmusic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musics',
            name='user',
        ),
        migrations.AddField(
            model_name='users',
            name='title',
            field=models.ManyToManyField(to='usersmusic.Musics'),
        ),
    ]
