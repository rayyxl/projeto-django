from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listar_pessoas/', views.listar_pessoas, name='listar_pessoas'),
    path('criar_pessoa/', views.criar_pessoa, name='criar_pessoa'),
    path('atualizar_pessoa/<int:id>/', views.atualizar_pessoa, name='atualizar_pessoa'),
    path('deletar_pessoa/<int:id>/', views.deletar_pessoa, name="deletar_pessoa")
]