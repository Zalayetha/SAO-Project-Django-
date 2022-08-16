from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views.generic.base import RedirectView
from django.contrib.auth import authenticate,login,logout

# @login_required(login_url='login')
def index(request):
     if request.user.is_authenticated:
          return render(request,'index_user.html')

     return render(request,'index.html')

def loginPage(request):
     # prevent authenticate user back to login page
     print(request.POST)
     if request.method == 'GET':
          if request.user.is_authenticated:
               print('berhasil')
               return redirect('index')

     # auth user login
     if request.method =='POST':
          username_user = request.POST['username']
          password_user = request.POST['password']

          usr = authenticate(request,username=username_user,password=password_user)
          print(usr)
          if usr is not None :
               login(request,usr)
               return redirect('index')

               
     return render(request,'login.html')

@login_required(login_url='index')
def logoutPage(request):
     if request.method == "POST":
          if request.POST['logout'] == 'Submit':
               logout(request)
               return redirect('index')

     return render(request,'logout.html')
     # logout(request)
     # return redirect('login')


class HomeParam(RedirectView):
     pattern_name='index'