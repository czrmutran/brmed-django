from django.urls import path, include
from app_brmed import views
from django.contrib import admin

urlpatterns = [
    # rota, view responsavel, nome de referencia 
    #brmed.com
    path('',views.home,name='home'),
   
    path('cadastro/',views.cadastro,name='cadastro'),
   
    path('usuarios/', views.usuarios,name='listagem_usuarios'),
    
    path('auth/', views.auth,name='auth'),
  
    path('agendamento/', views.agendamentos,name='agendamento'),

    path('marcados/', views.marcados,name='listagem_agendamentos')

]   
