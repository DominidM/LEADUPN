from django.urls import path
from . import views

urlpatterns = [
    path('',             views.home,       name='home'),
    path('clasificador/', views.formulario, name='formulario'),
    path('daisy/',        views.daisy,      name='daisy'),
    path('birds/',        views.birds,      name='birds'),
]