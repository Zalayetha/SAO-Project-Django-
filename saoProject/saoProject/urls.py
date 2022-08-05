from argparse import Namespace
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('blog/',include('blog.urls',namespace='blog')),
    path('contact/',include('contact.urls',namespace='contact')),
]
