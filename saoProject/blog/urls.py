from django import views
from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    re_path(r'^category/(?P<categoryInput>[\w-]+)/$',views.categoryPost,name='category'),
    re_path(r'^post/(?P<slugInput>[\w-]+)/$',views.detailPost,name='detail'),
    path('create/',views.create,name='create'),
]

app_name='blog'