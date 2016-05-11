from django import forms
from django.forms import ModelForm

from .models import Parent as parent_model

class CreateParentForm(ModelForm):
    """
    Form for Parent/Roditelj
    """
   
    first_name    = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input'}), required=True, max_length=30)
    last_name     = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input'}), required=True, max_length=30)
    jmbg          = forms.CharField(widget=forms.NumberInput(attrs={'class':'form_input'}), max_length=13)
    pid_num       = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form_input'}))
    address       = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input'}), max_length=45)
    mob_num       = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input'}), required=True)
    phone_num     = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input'}), max_length=30)
    company       = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input'}), max_length=30)
    city          = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form_input'}))
    email         = forms.CharField(widget=forms.EmailInput(attrs={'class':'form_input'}), max_length=100)
    employed      = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form_input'}), initial=True)
    workplace     = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input'}), max_length=30)
    note          = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40, 'class':'form_textarea'}), required=False)
    last_user     = forms.IntegerField(required=False)
    
    class Meta:
        model = parent_model
        fields = ['first_name', 'last_name', 'jmbg', 'pid_num', 'address', 'mob_num', 'phone_num', 'company',
                  'city', 'email', 'employed', 'workplace', 'note', 'last_user']
        
    def __init__(self, *args, **kwargs):
        self.last_user = kwargs.pop("last_user")
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['last_user'].initial = self.last_user
        
    def clean_last_user(self):
        last_user = self.cleaned_data['last_user']
        if last_user is None:
            last_user = self.last_user
        return last_user
    
class ParentAdvanceSearchParameters(forms.Form):
    first_name    = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control choice_field','id':'first_name'}),label = "Ime",max_length=15)
    last_name     = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control choice_field','id':'last_name'}),label = "Prezime",max_length=30)
    jmbg          = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control choice_field','id':'jmbg'}),label = "JMBG",max_length=13)
    address       = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control choice_field','id':'address'}),label = "Adresa",max_length=40)
