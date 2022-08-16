from django.urls import path,re_path
from .views import ClassView
urlpatterns = [
    path("",ClassView.as_view(template_name='contact/index.html'),name='index'),
]

app_name = 'contact'