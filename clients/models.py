from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class Parent(models.Model):
    first_name           = models.CharField(max_length=30)
    last_name            = models.CharField(max_length=30)
    jmbg                 = models.CharField(max_length=13, null=True, blank=True)
    pid_num              = models.IntegerField(null=True, blank=True)
    address              = models.CharField(max_length=50, null=True, blank=True)
    mob_num              = models.CharField(max_length=15)
    phone_num            = models.CharField(max_length=15, null=True, blank=True)
    company              = models.CharField(max_length=30, null=True, blank=True)
    city                 = models.IntegerField(null=True, blank=True)
    email                = models.CharField(max_length=40, null=True, blank=True)
    employed             = models.BooleanField(blank=True)
    workplace            = models.CharField(max_length=40, null=True, blank=True)
    note                 = models.CharField(max_length=255, null=True, blank=True)
    
    creation_date        = models.DateTimeField(auto_now_add=True)
    modification_date    = models.DateTimeField(auto_now=True)
    last_user            = models.ForeignKey(User)
    #created              = models.ForeignKey(User)
    
