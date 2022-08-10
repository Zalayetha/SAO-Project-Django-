from django import forms
from .models import Post
# class CreatePost(forms.Form):
#      subject = forms.CharField(
#           max_length=50,
#           widget=forms.TextInput(
#                attrs={
#                     'class':'form-control'
#                }
#           ))
#      category = forms.CharField(
#           max_length=50,
#           widget=forms.TextInput(
#                attrs={
#                     'class':'form-control'
#                }
#           ))
#      body = forms.CharField(
#           widget=forms.Textarea(
#                attrs={
#                     'class':'form-control'
#                }
#           )
#      )

#      def clean_category(self):
#           data_category = Post.objects.values('category').distinct()
#           category_input = self.cleaned_data.get("category")

#           for data in data_category:
#                print(data)
#                if category_input == data['category']:
#                     break     
#                else:
#                     print('eror')
#                     raise forms.ValidationError("ucup tidak boleh diposting")

#           return category_input

class CreatePost(forms.ModelForm):
     class Meta:
          model = Post
          fields=[
               'subject',
               'category',
               'body',
          ]
          widgets = {
               'subject':forms.TextInput(
                    attrs={
                         'class':'form-control',
                    }
                    ),
               'category':forms.Select(
                    attrs={
                         'class':'form-control',
                    }
               ),
               'body':forms.Textarea(
                    attrs={
                         'class':'form-control',
                    }
               ),
          }