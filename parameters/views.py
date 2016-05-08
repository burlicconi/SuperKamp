# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import (HttpResponse,)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ParTable
from .models import ParLine
from .forms import SearchParTablesForm
from .forms import CreateParTableForm
from .forms import CreateParTableLineForm
from .forms import TableAdvanceSearchParameters
from .forms import LineAdvanceSearchParameters


@login_required
def search_tables(request):
    search_tables_form = SearchParTablesForm()
    context = {"search_tables_form" : search_tables_form}
    return render(request,'parameters/search_tables.html',context)

@login_required
def create_table(request):
    table_details = CreateParTableForm(last_user = request.user)
    context = {"table_details" : table_details}
    return render(request,'parameters/table_details.html',context)

@login_required
def show_tables(request, ptable='-1', ptabdesc='-1'):
    if request.method == 'POST':
        ptable = request.POST.get("table_no", "")
        ptabdesc = request.POST.get("table_desc", "")

    # create filters and get results from DB
    query_filters = {}
    if (ptable is None or ptable.strip() != '') and ptable != '-1':
        query_filters['table_no'] = ptable
    if (ptabdesc is None or ptabdesc.strip() != '') and ptabdesc != '-1':
        query_filters['table_desc__icontains'] = ptabdesc
          
    if len(query_filters) > 0:
        result_tables = ParTable.objects.filter(**query_filters)
    else:
        result_tables = ParTable.objects.all().order_by('table_no')

    form = TableAdvanceSearchParameters()
    context = {"result_tables" : result_tables, "form" : form}
    return render(request,'parameters/show_tables.html',context)
        
@login_required
def save_table(request, ptable=-999):

    if request.method == 'POST':
        
        if ptable == -999:  # ptable is not defined
            form = CreateParTableForm(request.POST, request.FILES,last_user=request.user)
            if form.is_valid():
                form.save()
            else:
                print form.errors
        else:
            tmp_par_tabl = ParTable.objects.get(pk=ptable)
            table_details = CreateParTableForm(request.POST, request.FILES, instance=tmp_par_tabl)
            if table_details.is_valid():
                tmp_par_tabl.save()
        
        return show_tables(request, ptable)
            
    else:
        messages.error(request, "Error 002")
        return HttpResponse("Error 002")
        
    context = {"create_table" : create_table}
    return render(request, 'parameters/create_table.html', context)

@login_required
def delete_table(request, ptable):
    tmp_table_no = ParTable.objects.filter(table_no=ptable)
    tmp_table_no.delete()
    return show_tables(request)

@login_required
def edit_table(request, ptable):
    tmp_par_tabl = ParTable.objects.get(pk=ptable)
    table_details = CreateParTableForm(instance=tmp_par_tabl,last_user=request.user)
    table_details.fields['table_no'].widget.attrs['readonly'] = True
    context = {"table_details" : table_details, "ptable" : ptable}
    return render(request,'parameters/table_details.html',context)

@login_required
def show_lines(request, ptable, pline='-1', plinedesc='-1'):
    if ptable is None or ptable.strip() == '':
        messages.error(request, "Error 003")
        return HttpResponse("Error 003")
    
    if request.method == 'POST':
        pline = request.POST.get("line_no", "")
        plinedesc = request.POST.get("line_desc", "")
    
    query_filters = {}
    query_filters['table_no'] = ptable
    if (pline is None or pline.strip() != '') and pline != '-1':
        query_filters['line_no'] = pline
    if (plinedesc is None or plinedesc.strip() != '') and plinedesc != '-1':
        query_filters['line_desc__icontains'] = plinedesc
          
    if len(query_filters) > 0:
        result_lines = ParLine.objects.filter(**query_filters).order_by('line_no')
    else:
        result_lines = ParLine.objects.filter(table_no = ptable).order_by('line_no')
        
    headerTitle = (ParTable.objects.get(pk = ptable)).table_desc

    form = LineAdvanceSearchParameters()
    context = {"result_lines" : result_lines, "ptable" : ptable, "header_title" : headerTitle, "form" : form}
    return render(request,'parameters/show_lines.html',context)

@login_required
def create_line(request, ptable, form=None):
    if form==None:#creating new
        line_details = CreateParTableLineForm(last_user = request.user,table_no=ptable)
        context = {"line_details" : line_details, "ptable" : ptable}
    else:#updating existing
        context = {"line_details" : form, "ptable" : ptable}
    return render(request,'parameters/line_details.html',context)

@login_required
def save_line(request, ptable, pline=-999):
    print 'save line', ptable, pline
    if request.method == 'POST':
        print 'post'
        if pline == -999:# line is not defined, create new
            form = CreateParTableLineForm(request.POST, request.FILES,last_user=request.user, table_no=ptable)
            try:
                if form.is_valid():
                    form.save()
                else:
                    print 'errors2',form.errors
                    context = {"create_line" : create_line, "ptable" : ptable, 'errors': form.errors}
                    print 'contex', context
                    return render(request, reverse('parameters:create_line', kwargs={'ptable': ptable}))
                
            except Exception as e:
                print e
                print 'usao u exc, greske su: ', form.errors
                return create_line(request, ptable, form)
                
        else:
            tmp_par_line = ParLine.objects.filter(table_no=ptable, line_no=pline)[0]
            tmpForm = request.POST.copy()
            tmpForm['table_no'] = ptable
            tmpForm['last_user'] = request.user
            line_details = CreateParTableLineForm(tmpForm, request.FILES, instance=tmp_par_line)
            if line_details.is_valid():
                tmp_par_line.save()
            else:
                print line_details.errors
                
        return show_lines(request, ptable)
        
    else:
        messages.error(request, "Error 004")
        return HttpResponse("Error 004")
        
    context = {"create_table" : create_table}
    return render(request, 'parameters/create_table.html', context)

@login_required
def delete_line(request, ptable, pline):
    tmp_line_no = ParLine.objects.filter(table_no=ptable, line_no=pline)
    tmp_line_no.delete()
    return show_lines(request, ptable)

@login_required
def edit_line(request, ptable, pline):
    tmp_line_no = ParLine.objects.filter(table_no=ptable, line_no=pline)[0]
    line_details = CreateParTableLineForm(instance=tmp_line_no)
    line_details.fields['line_no'].widget.attrs['readonly'] = True
    context = {"line_details" : line_details, "ptable" : ptable, "pline" : pline}
    return render(request,'parameters/line_details.html',context)