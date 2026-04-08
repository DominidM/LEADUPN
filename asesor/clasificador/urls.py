from django.urls import path
from . import views

urlpatterns = [
    path('',       views.formulario, name='formulario'),
    path('lista/', views.lista,       name='lista'),
]