# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from . import views
 
urlpatterns = [
               url(r'^search_tables/$',views.search_tables, name="search_tables"),
               url(r'^tables/(?P<ptable>\w+)/(?P<ptabdesc>\w+)/$',views.show_tables, name="show_tables"),
               url(r'^tables/(?P<ptable>\w+)/$',views.show_tables, name="show_tables"),
               url(r'^tables/$',views.show_tables, name="show_tables"),
               url(r'^create_table/$',views.create_table, name="create_table"),
               url(r'^save_table/(?P<ptable>\w+)/$',views.save_table, name="save_table"),
               url(r'^save_table/$',views.save_table, name="save_table"),
               url(r'^delete_table/(?P<ptable>\w+)/$',views.delete_table, name="delete_table"),
               url(r'^edit_table/(?P<ptable>\w+)/$',views.edit_table, name="edit_table"),
               url(r'^show_lines/(?P<ptable>\w+)/$',views.show_lines, name="show_lines"),
               url(r'^create_line/(?P<ptable>\w+)/$',views.create_line, name="create_line"),
               url(r'^save_line/(?P<ptable>\w+)/(?P<pline>\w+)/$',views.save_line, name="save_line"),
               url(r'^save_line/(?P<ptable>\w+)/$',views.save_line, name="save_line"),
               url(r'^delete_line/(?P<ptable>\w+)/(?P<pline>\w+)/$',views.delete_line, name="delete_line"),
               url(r'^edit_line/(?P<ptable>\w+)/(?P<pline>\w+)/$',views.edit_line, name="edit_line"),
               ]