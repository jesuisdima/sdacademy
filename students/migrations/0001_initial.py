# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'\xd0\xb8\xd0\xbc\xd1\x8f', max_length=32)),
                ('surname', models.CharField(help_text=b'\xd1\x84\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f', max_length=64)),
                ('date_of_birth', models.DateField(help_text=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(help_text=b'\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd', max_length=32)),
                ('address', models.CharField(help_text=b'\xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81', max_length=255)),
                ('skype', models.CharField(max_length=32)),
                ('courses', models.ManyToManyField(help_text=b'\xd0\xba\xd1\x83\xd1\x80\xd1\x81\xd1\x8b, \xd0\xbd\xd0\xb0 \xd0\xba\xd0\xbe\xd1\x82\xd0\xbe\xd1\x80\xd1\x8b\xd1\x85 \xd1\x83\xd1\x87\xd0\xb8\xd1\x82\xd1\x81\xd1\x8f \xd1\x81\xd1\x82\xd1\x83\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82', to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
