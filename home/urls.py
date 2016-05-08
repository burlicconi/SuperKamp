from . import views
from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('home.views',
               url(r'^login$',views.login_view, name='login'),
               url(r'^login(?P<next>.+)',views.login_view, name='login'),
               url(r'^logout$', views.logout_view,name='logout'),
               )