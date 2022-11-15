from django import forms
from .models import *

class regform(forms.ModelForm):
    class Meta:
        model=regmodel
        fields=('fname','email','password','phoneNumber','gen','adrs','District')
        widigets={
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'phoneNumber':forms.TextInput(attrs={'class':'form-control'}),
            'gen':forms.TextInput(attrs={'class':'form-control'}),
            'adrs':forms.TextInput(attrs={'class':'form-control'}),
            'District':forms.TextInput(attrs={'class':'form-control'}),
        }

class orphanageuserform(forms.ModelForm):
    class Meta:
        model=orphanage_user
        fields=('name','aadhaar_no','age','gender','address','DOB','img')
        widigets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'aadhaar_no':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'DOB':forms.TextInput(attrs={'class':'form-control'}),
            'img':forms.TextInput(attrs={'class':'form-control'}),
        }

class orphanageform(forms.ModelForm):
    class Meta:
        model=orphanagemodel
        fields=('orphanage_name','owner_name','address','contact_no','email','location')
        widigets={
                'orphanage_name':forms.TextInput(attrs={'class':'form-control'}),
                'owner_name':forms.TextInput(attrs={'class':'form-control'}),
                'address':forms.TextInput(attrs={'class':'form-control'}),
                'contact_no':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.TextInput(attrs={'class':'form-control'}),
                'location':forms.TextInput(attrs={'class':'form-control'}),
        }

class donationform(forms.ModelForm):
    class Meta:
        model=donationmodel
        fields=('username','Orphanagename','amount')
        widigets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'Orphanagename':forms.TextInput(attrs={'class':'form-control'}),
            'amount':forms.TextInput(attrs={'class':'form-control'}),
        }
