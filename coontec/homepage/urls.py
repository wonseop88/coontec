'''
Created on 2017. 3. 20.

@author: wonseop
'''

from django.conf.urls import include, url
from . import views
from . import emailSend


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^solution/(?P<page_url>\w+)/$', views.page, name='solution'),
    url(r'^product/(?P<page_url>\w+)/$', views.page, name='product'),
    url(r'^company/(?P<page_url>\w+)/$', views.page, name='company'),
    url(r'^resource/(?P<page_url>\w+)/$', views.page, name='resource'),
    url(r'^service/(?P<page_url>\w+)/$', views.page, name='service'),
    url(r'^emailsend/$', emailSend.send_email, name='email'),

]