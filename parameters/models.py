# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class ParTable(models.Model):
    table_no          = models.PositiveIntegerField(primary_key=True)
    table_desc        = models.CharField(max_length=100)
    table_comment     = models.CharField(max_length=1000, blank=True, null=True)
    table_num1        = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    table_num2        = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    table_num3        = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    table_num4        = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    creation_date     = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    last_user         = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.table_desc
    
class ParLine(models.Model):
    table_no          = models.ForeignKey(ParTable)
    line_no           = models.PositiveIntegerField()
    line_desc         = models.CharField(max_length=100)
    line_comment      = models.CharField(max_length=1000, blank=True, null=True)
    line_num1         = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    line_num2         = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    line_num3         = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    line_num4         = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    line_alpha1       = models.CharField(max_length=30, blank=True, null=True)
    line_alpha2       = models.CharField(max_length=60, blank=True, null=True)
    line_date1        = models.DateField(blank=True, null=True)
    line_date2        = models.DateField(blank=True, null=True)
    creation_date     = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    last_user         = models.ForeignKey(User)
    
    class Meta:
        unique_together = (("table_no", "line_no"))
        
    def __unicode__(self):
        return self.line_desc
    
    def save(self):
        if self.line_alpha1=="":
            self.line_alpha1 = None
        if self.line_alpha2=="":
            self.line_alpha2 = None
        super(ParLine, self).save()
