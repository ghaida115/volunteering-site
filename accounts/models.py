from django.db import models

# Create your models here.
from userena.models import UserenaBaseProfile

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    cv = models.FileField
    favourite_snack = models.CharField(_('favourite snack'),
                                       max_length=5)

class institute(models.Model):
    name = models.CharField
    description = models.CharField

class comments(models.Models) :
    institute = models.Forienkey
    user = models.OneToOne
    text = models.Charfield
    date = models.DateTimeField

class volunteer_work(models.Models) :
    institute = models.Forienkey
    description = models.CharField
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
