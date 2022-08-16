from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from django.views.generic.base import RedirectView,TemplateView
from .views import HomeParam
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('blog/',include('blog.urls',namespace='blog')),
    path('contact/',include('contact.urls',namespace='contact')),
    path('profilechar/',include('profilechar.urls',namespace='profile')),
    re_path(r'home/',RedirectView.as_view(pattern_name='index'),name='redirectHome'),
    # re_path(r'test/(?P<param>[\w-]+)',HomeParam.as_view(),name='homeparam'),
    # re_path(r'(?P<param>[\w-]+)',TemplateView.as_view(template_name='index.html'),name='index'),
]
