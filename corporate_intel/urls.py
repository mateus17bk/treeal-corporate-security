from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('consultar/', views.consultar_cnpj_view, name='consultar_cnpj'),
    path('empresa/<int:pk>/', views.detalhes_empresa_view, name='detalhes_empresa'),
    path('historico/', views.historico_view, name='historico'),
]
