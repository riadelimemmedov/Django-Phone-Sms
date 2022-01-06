from django import forms
from .models import  *

class CodeForm(forms.ModelForm):#ModelForm yazilmaisndaki esas sebeb biz siirdan form yaratmitig movcut modelcek cekib istifade edirik,eger sifirdan bir form yaratmag isteyirnsese forms.Form dan istifade et
    number = forms.CharField(label='Code',help_text='Enter SMS Verification')#help_text bir cur htmldeki placeholder isini gorur help_text
    
    class Meta:
        model = Code
        fields = ['number']#istifadeci html de number girecek 