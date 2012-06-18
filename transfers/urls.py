from django.conf.urls import patterns, include, url
from django.views.generic import ListView,DetailView
from transfers.models import Transfer
from transfers.views import description_ListView, plan_ListView, my_ListView


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^load/','transfers.views.load'),
                       url(r'^$',
                           ListView.as_view(
                            model = Transfer,
                            paginate_by = 15, #todo:show pagination in page
                            #page = request.Get.get('page'),
                            
                            context_object_name = 'all_transfers',
                            template_name ='transfers/index.html',
                            
                           ),),
                       url(r'^(?P<pk>\d+)/$',
                           DetailView.as_view(
                            model = Transfer,                           
                            template_name = 'transfers/detail.html' #todo:protect from no such transfer
                           ),name = 'base_transfer'),
                       
                       url (r'^plan/(?P<plan_name>[\w ]+)/$',
                            my_ListView(
                            property = 'plan_name',
                            title ='planname',
                            template_name = 'transfers/plan.html'
                            ), name = 'plan_url'),
                       #url(r'^plan/(?P<plan_name>[\w ]+)/$',
                       #    'transfers.views.plan_ListView',
                       #    name = 'plan_url'),
                       
                        url(r'^description/(?P<description>[\w ]+)/$',
                            'transfers.views.description_ListView',
                            name = 'description_url')
                       )
                       
