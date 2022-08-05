from django.shortcuts import render
from .contact import ContactPerson
# Create your views here.
def index(request):
     contact = ContactPerson()
     print(request.POST)
     context={
          'title' : 'Contact',
          'subTitle': "Welcome To Underworld Contact Form",
          'Contact' : contact,
     }
     return render(request,"contact/index.html",context)


