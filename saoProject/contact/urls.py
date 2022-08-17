from django.urls import path,re_path
from .views import index
urlpatterns = [
    # path("",ClassView.as_view(template_name='contact/index.html'),name='index'),
    path("",index,name='index')
]

app_name = 'contact'