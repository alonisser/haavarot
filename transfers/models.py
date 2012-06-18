# -*- coding: utf_8 -*-
from django.db import models
from django.db.models import permalink
from datetime import datetime

#from django.utils import timezone
class Error(models.Model):
    timestamp = models. DateTimeField()
    line_num = models.IntegerField()
    problem = models.CharField(max_length=200)
    
class Transfer(models.Model):
    line_num = models.IntegerField()#not sure if I should keep it
    year = models.IntegerField(u'השנה')
    section = models.IntegerField()
    request = models.IntegerField(u'בקשה')
    description =models.CharField(u'תיאור בקשה',max_length=200)
    change_code = models.IntegerField(u'קוד שינוי')
    change_name = models.CharField(u'שינוי',max_length=200)
    request_code = models.IntegerField(u'קוד בקשה')
    request_type = models.CharField(u'סוג בקשה',max_length=100)
    committee_num = models.IntegerField(u'מספר ועדה')
    plan_code = models.IntegerField(u'קוד תוכנית')
    plan_name = models.CharField(u'שם תוכנית',max_length=200)
    sum_neto = models.IntegerField(u'סכום נטו')
    sum_conditional = models.IntegerField(u'סכום מותנה')
    planned_income = models.IntegerField(u'הכנה צפויה')
    sum_permission = models.IntegerField(u'הגבלה להתחייבות')
    max_jobs = models.FloatField(u'שיא משרות')
    
    def __unicode__(self):
        return self.plan_name+u" סכום: " +unicode(self.sum_neto)
        
    
    def is_this_year(self):
        return datetime.now().timetuple().tm_year-self.year<1
    is_this_year.boolean = True
    is_this_year.short_description =u'מהשנה הנוכחית?'
    
    def abs_sum_neto(self):
        return abs(self.sum_neto)
    
    @permalink    
    def get_absolute_url(self):
        return "/transfers/%s" % self.description
        
# Create your models here.
