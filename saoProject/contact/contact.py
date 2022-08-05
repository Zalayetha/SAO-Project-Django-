from cProfile import label
from django import forms

class ContactPerson(forms.Form):
     fname = forms.CharField(
          label='First name',
          widget= forms.TextInput(
          attrs={
               'class':'form-control',
          })
     )
     lname = forms.CharField(
          label='Last Name',
          widget= forms.TextInput(
          attrs={
               'class':'form-control',
          })
     )
     email = forms.EmailField(
          label='Email',
          widget= forms.EmailInput(
               attrs={
                    'class':'form-control',
               }
          )
     )
     msg = forms.CharField(
          label='Message',
          widget= forms.Textarea(
               attrs={
                    'class':'form-control',
               }
          )
     )