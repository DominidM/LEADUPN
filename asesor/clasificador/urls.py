from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('daisy/', views.daisy, name='daisy'),       
]