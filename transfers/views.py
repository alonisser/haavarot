# -*- coding: utf_8 -*-

# Create your views here.
import csv
from datetime import datetime
from django.utils import timezone

from transfers.models import Transfer, Error
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
    #todo:only authenticated admin
    #todo:better error logging
    #todo:show a 'loading' gif/canvas while loading, even better - status reports
    file = open("transfers/changes_2011.csv",'rb',)
    #print (file)
    changes_to_load = unicode_csv_reader(file)
    
    for k,row in enumerate(changes_to_load):
        #print (row)
        try:
            o = Transfer(line_num = k,
                         year = row[0],
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
            print ('saved:', o)
            
        except Exception as e:
            print ('some error in line:',k)
            error = Error(line_num = k, timestamp = timezone.now(), problem = e)
            error.save()
            continue
            #print (0)

    file.close()
    print ('Loading Ended')
    return ('<p>loading done</p>') #todo:return something more useful with some statistics..file name, number of raws

    
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
