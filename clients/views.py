# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import (HttpResponse,)

from .forms import CreateParentForm, ParentAdvanceSearchParameters
from .models import Parent

#@login_required
def create_parent(request):
    """
    view for entering save/edit parent
    """
    parent_details = CreateParentForm(last_user = request.user)
    context = {"parent_details" : parent_details}
    return render(request,'clients/create_parent.html',context)

#@login_required
def preview_parent(request, parent_id):
    """
    view for entering save/edit parent
    """
    parent = Parent.objects.get(id=parent_id)
    parent_details = CreateParentForm(instance=parent,last_user=request.user)
    #print 'parent_details', parent_details
    #parent_details = CreateParentForm(parent_detail, last_user = request.user)
    #print 'parent_details',parent_details
    #parent_details["last_user"] = request.user
    context = {"parent_details" : parent_details, "save_button":"hidden"}
    return render(request,'clients/create_parent.html',context)

#@login_required
def save_parent(request, parent_id=-999):
    """
    view for saving parent (new or edited)
    """
    if request.method == 'POST':
        
        if parent_id == -999:  # parent is not defined
            form = CreateParentForm(request.POST, request.FILES,last_user=request.user)
            if form.is_valid():
                form.save()
            else:
                parent_details = CreateParentForm(request.POST, request.FILES, last_user=request.user)
                print form.errors
                context = {"parent_details" : form}
                return render(request, 'clients/create_parent.html', context) 
        else:
            tmp_parent = Parent.objects.get(pk=parent_id)
            parent_details = CreateParentForm(request.POST, request.FILES, instance=tmp_parent, last_user=request.user)
            if parent_details.is_valid():
                tmp_parent.save()
        return show_parents(request, parent_id)
            
    else:
        messages.error(request, "Error 002")
        return HttpResponse("Error 002")
        
    context = {"create_parent" : create_parent}
    return render(request, 'clients/create_parent.html', context)

#@login_required
def show_parents(request, parent_id='-1', parent_first_name='-1'):

    if request.method == 'POST':
        parent_id = request.POST.get("parent_id", "")
        #ptabdesc = request.POST.get("table_desc", "")

    # create filters and get results from DB
    query_filters = {}
    if (parent_id is None or parent_id.strip() != '') and parent_id != '-1':
        query_filters['id'] = parent_id
    if (parent_first_name is None or parent_first_name.strip() != '') and parent_first_name != '-1':
        query_filters['first_name'] = parent_first_name
          
    if len(query_filters) > 0:
        result_tables = Parent.objects.filter(**query_filters)
    else:
        result_tables = Parent.objects.all().order_by('id')

    form = ParentAdvanceSearchParameters()
    context = {"result_tables" : result_tables, "form" : form}
    return render(request,'clients/show_parents.html',context)

#@login_required
def edit_parent(request, parent_id):
    tmp_parent = Parent.objects.get(pk=parent_id)
    parent_details = CreateParentForm(instance=tmp_parent, last_user=request.user)
    #parent_details.fields['parent_id'].widget.attrs['readonly'] = True
    context = {"parent_details" : parent_details, "parent_id" : parent_id}
    return render(request,'clients/create_parent.html',context)

#@login_required
def delete_parent(request, parent_id):
    parent = Parent.objects.filter(id=parent_id)
    parent.delete()
    return show_parents(request)