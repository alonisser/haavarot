# -*- coding: utf_8 -*-
from transfers.models import Transfer, Error
from django.contrib import admin


class TransferAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'התוכנית:',{'fields':['plan_name',
                               'plan_code',
                               'year',
                               'sum_neto',
                               'sum_conditional',
                               'planned_income',
                               'sum_permission',
                               'max_jobs']}),
        (u'טכני העברה: ',{'fields':['section',
                                   'request',
                                   'description',
                                   'change_code',
                                   'change_name',
                                   'request_code',
                                   'request_type',
                                   'committee_num'],
                        'classes':['collapse']
                        })
    ]
    search_fields = ['plan_name','committee_num','description','change_name']
    list_display = ('plan_name','sum_neto','is_this_year','request_type','change_name')
    list_filter =['request_type','change_name','plan_name']
    
admin.site.register(Transfer,TransferAdmin)
admin.site.register(Error)
#admin.site.register(Transfer,TransferAdmin)