from django.shortcuts import render
from .contact import ContactPerson
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.
def index(request):
     contact = ContactPerson()
     context={
          'title' : 'Contact',
          'subTitle': "Welcome To Underworld Contact Form",
          'Contact' : contact,
     }
     # if request.user.is_authenticated:
     #      return render(request,"contact/index_user.html",context)
          
     return render(request,"contact/index.html",context)


# class ClassView(View):
#      template_name = ''
#      contact = ContactPerson()
#      context = {}

#      def get(self,request):
#           self.context={
#                'title':'Contact',
#                'subTitle':'Welcome To Underworld Contact Form',
#                'Contact':self.contact,
#           }

#           return render(request,self.template_name,self.context)


# class ClassView(TemplateView):
#      template_name=''
#      contact = ContactPerson()
#      def get_context_data(self):
#           context = {
#                'title':'Contact',
#                'subTitle':'Welcome To Underworld Contact Form',
#                'Contact':self.contact,
#           }
#           return context

        


