# -*- coding: utf-8 -*-

from functools import partial

from django import forms
from django.forms import ModelForm

from .models import ParTable
from .models import ParLine

class SearchParTablesForm(ModelForm):    
    class Meta:
        model = ParTable
        fields = ['table_no','table_desc']
                    
class CreateParTableForm(ModelForm):
    table_comment = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40, 'class':'form_textarea'}), required=False)
    table_no      = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form_input'}))
    table_desc    = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input'}))
    table_num1    = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form_input'}),required=False)
    table_num2    = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form_input'}),required=False)
    table_num3    = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form_input'}),required=False)
    table_num4    = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form_input'}),required=False)
    last_user     = forms.IntegerField(required=False)
    
    class Meta:
        model = ParTable
        fields = ['table_no', 'table_desc', 'table_comment', 'table_num1', 'table_num2', 'table_num3', 'table_num4', 'last_user']
    
    def __init__(self, *args, **kwargs):
        self.last_user = kwargs.pop("last_user")
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['last_user'].initial = self.last_user
        
    def clean_last_user(self):
        last_user = self.cleaned_data['last_user']
        if last_user is None:
            last_user = self.last_user
        return last_user


        
class CreateParTableLineForm(ModelForm):
    DateInput    = partial(forms.DateInput, {'class': 'form_input'})
    line_num1    = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form_input'}),required=False)
    line_num2    = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form_input'}),required=False)
    line_num3    = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form_input'}),required=False)
    line_num4    = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form_input'}),required=False)
    line_date1   = forms.DateField(widget=DateInput(), required=False)
    line_date2   = forms.DateField(widget=DateInput(), required=False)
    line_no      = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form_input'}),required = True)
    line_desc    = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input'}))
    line_comment = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40, 'class':'form_textarea'}), required=False)
    line_alpha1  = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input'}),required=False)
    line_alpha2  = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input'}),required=False)
    last_user    = forms.IntegerField(required=False)
    table_no     = forms.IntegerField(required=False)
    
    class Meta:
        model = ParLine
        fields = ['table_no', 'line_no', 'line_desc', 'line_comment', 'line_num1', 'line_num2', 'line_num3', 'line_num4', 
                  'line_alpha1', 'line_alpha2', 'line_date1', 'line_date2', 'last_user']
    
    def __init__(self, *args, **kwargs):
        self.last_user = kwargs.pop("last_user")
        self.table_no = ParTable.objects.get(pk=kwargs.pop("table_no"))
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['last_user'].initial = self.last_user
        self.fields['table_no'].initial = self.table_no
        
    def clean_last_user(self):
        last_user = self.cleaned_data['last_user']
        if last_user is None:
            last_user = self.last_user
        return last_user
    
    def clean_table_no(self):
        table_no = self.cleaned_data['table_no']
        if table_no is None:
            table_no = self.table_no
        return table_no
    
class TableAdvanceSearchParameters(forms.Form):
    table_no     = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control choice_field','id':'table_no'}),label = "Broj tabele",max_length=15)
    table_desc   = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control choice_field','id':'table_desc'}),label = "Opis tabele",max_length=100)   

class LineAdvanceSearchParameters (forms.Form):
    line_no      = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'number','class':'form-control choice_field','id':'line_no'}),label = "Broj linije")
    line_desc    = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control choice_field','id':'line_desc'}),label = "Opis atributa description",max_length=100)