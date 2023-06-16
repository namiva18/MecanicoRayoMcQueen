from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('quiensomos/', views.quiensomos, name='quiensomos'),
    path('trab_real/', views.trab_real, name='trab_real'),
    path('caja_cambio/', views.caja_cambio, name='caja_cambio'),
    path('electro/', views.electro, name='electro'),
    path('suspension/', views.suspension, name='suspension'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login, name='login'),
    path('plantilla/', views.plantilla, name='plantilla'),
    path('registro/', views.registro, name='registro'),

]