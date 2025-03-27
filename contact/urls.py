from django.urls import path
from contact import views

app_name = 'contact' #namespace 

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'), 
    path('', views.index, name='index'), 
]
