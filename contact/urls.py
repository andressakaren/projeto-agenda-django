from django.urls import path
from contact import views

app_name = 'contact' #namespace 

urlpatterns = [
    path('', views.index, name='index'), 
]
