# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views
 
urlpatterns = [
               url(r'^create_parent/$',views.create_parent, name="create_parent"),
               url(r'^preview_parent/(?P<parent_id>\w+)/$',views.preview_parent, name="preview_parent"),
               url(r'^save_parent/$',views.save_parent, name="save_parent"),
               url(r'^save_parent/(?P<parent_id>\w+)/$',views.save_parent, name="save_parent"),
               url(r'^edit_parent/(?P<parent_id>\w+)/$',views.edit_parent, name="edit_parent"),
               url(r'^delete_parent/(?P<parent_id>\w+)/$',views.delete_parent, name="delete_parent"),
               url(r'^show_parents/$',views.show_parents, name="show_parents"),
               ]