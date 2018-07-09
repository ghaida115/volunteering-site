# -*- coding: utf-8  -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from userena.models import UserenaBaseProfile


class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=('user'),
                                related_name='my_profile')
    cv = models.FileField

class institute(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)

class comments(models.Model) :
    institute = models.ForeignKey(institute)
    user = models.OneToOneField(User)
    text = models.CharField(max_length = 300)
    date = models.DateTimeField()

class volunteer_work(models.Model) :
    institute = models.ForeignKey (institute)
    description = models.CharField(max_length = 300)
    release_date = models.DateTimeField (null=True)
    submission_date = models.DateTimeField (auto_now_add=True)
    work_choices = (
    ('', '--'),
    ('R', 'تغطية إعلامية'),
    ('J', 'تنظيم ميداني'),
    ('A', 'تقديم ورشة عمل'),
    ('S', 'إدارة'),
)
    city = models.CharField("العمل التطوعي", max_length=1,
                            choices=work_choices)
