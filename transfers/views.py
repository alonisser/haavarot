# -*- coding: utf_8 -*-

# Create your views here.
import csv
from datetime import datetime
from django.utils import timezone

from transfers.models import Transfer
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse    
from django.template import Context,loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic import ListView

#later change this to something not hardcoded
def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'windows-1255') for cell in row]
        
def load(request):
    
    file = open("transfers/changes_2011.csv",'rb',)
    print (file)
    changes_to_load = unicode_csv_reader(file)
    for row in changes_to_load:
        print (row)
        o = Transfer(year = row[0],
                     section = row[1],
                     request = row[2],
                     description = row[3],
                     change_code = row[4],
                     change_name = row[5],
                     request_code = row[6],
                     request_type = row[7],
                     committee_num = row[8],
                     plan_code = row[9],
                     plan_name = row[10],
                     sum_neto = int(''.join(row[11].split(','))),
                     sum_conditional = int(''.join(row[12].split(','))),
                     planned_income = int(''.join(row[13].split(','))),
                     sum_permission = int(''.join(row[14].split(','))),
                     max_jobs = row[15]
                     )
        o.save()
        print ('saved')
        print (0)

    file.close()
    print ('ended')
    return ('<p>loading done</p>')

def plan_ListView(request,**kwargs):
    
    template_name = 'transfers/plan.html'
    #print ("template: ", template_name)
    
    o = get_list_or_404(Transfer, plan_name =kwargs['plan_name'])
    #print ('o:',o)
    context_object_name = "transfers_list" 
    return render_to_response(template_name,{context_object_name:o,'planname':kwargs['plan_name']})
    
    
def description_ListView(request,**kwargs):
    
    template_name = 'transfers/description.html'
        
    o = get_list_or_404(Transfer, description =kwargs['description'])
        #print ('o:',o)
    context_object_name = "transfers_list" 
    return render_to_response(template_name,{context_object_name:o,'description':kwargs['description']})
