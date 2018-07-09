# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields
from django.conf import settings
import userena.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=300)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='institute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mugshot', easy_thumbnails.fields.ThumbnailerImageField(help_text='A personal image displayed in your profile.', upload_to=userena.models.upload_to_mugshot, verbose_name='mugshot', blank=True)),
                ('privacy', models.CharField(default=b'registered', help_text='Designates who can view your profile.', max_length=15, verbose_name='privacy', choices=[(b'open', 'Open'), (b'registered', 'Registered'), (b'closed', 'Closed')])),
                ('user', models.OneToOneField(related_name='my_profile', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'permissions': (('view_profile', 'Can view profile'),),
            },
        ),
        migrations.CreateModel(
            name='volunteer_work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=300)),
                ('release_date', models.DateTimeField(null=True)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(max_length=1, verbose_name='\u0627\u0644\u0639\u0645\u0644 \u0627\u0644\u062a\u0637\u0648\u0639\u064a', choices=[('', '--'), ('R', '\u062a\u063a\u0637\u064a\u0629 \u0625\u0639\u0644\u0627\u0645\u064a\u0629'), ('J', '\u062a\u0646\u0638\u064a\u0645 \u0645\u064a\u062f\u0627\u0646\u064a'), ('A', '\u062a\u0642\u062f\u064a\u0645 \u0648\u0631\u0634\u0629 \u0639\u0645\u0644'), ('S', '\u0625\u062f\u0627\u0631\u0629')])),
                ('institute', models.ForeignKey(to='accounts.institute')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='institute',
            field=models.ForeignKey(to='accounts.institute'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
