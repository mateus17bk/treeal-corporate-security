from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('consultar/', views.consultar_cnpj_view, name='consultar_cnpj'),
    path('empresa/<int:pk>/', views.detalhes_empresa_view, name='detalhes_empresa'),
    path('historico/', views.historico_view, name='historico'),
    path('cadastro/', views.registrar_usuario_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
