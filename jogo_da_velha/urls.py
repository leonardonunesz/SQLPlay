from django.urls import path
from . import views

app_name = 'jogo_da_velha'

urlpatterns = [
    path('', views.jogo_da_velha, name='jogo_da_velha'),
    path('executar-sql/', views.executar_sql, name='executar_sql'),
    path('novo-jogo/', views.novo_jogo, name='novo_jogo'),
    path('estado-jogo/', views.obter_estado_jogo, name='estado_jogo'),
]
