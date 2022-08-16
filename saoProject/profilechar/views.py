from django.shortcuts import render

# Create your views here.
def index(request):
     context={
          'title':'Profile',
          'subTitle':'Welcome to Profile Page',
     }

     return render(request,'profilechar/index.html',context)