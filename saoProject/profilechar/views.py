from django.shortcuts import render
# from django.contrib.auth.models import 
# Create your views here.
def index(request):
     context={
          'title':'Profile',
          'subTitle':'Welcome to Profile Page',
     }


     return render(request,'profilechar/index.html',context)