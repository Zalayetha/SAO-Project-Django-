from django import forms

class CreatePost(forms.Form):
     subject = forms.CharField(
          max_length=50,
          widget=forms.TextInput(
               attrs={
                    'class':'form-control'
               }
          ))
     category = forms.CharField(
          max_length=50,
          widget=forms.TextInput(
               attrs={
                    'class':'form-control'
               }
          ))
     body = forms.CharField(
          widget=forms.Textarea(
               attrs={
                    'class':'form-control'
               }
          )
     )