from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views, api_status

urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('consultar/', views.consultar_cnpj_view, name='consultar_cnpj'),
    path('empresa/<int:pk>/', views.detalhes_empresa_view, name='detalhes_empresa'),
    path('historico/', views.historico_view, name='historico'),
    path('cadastro/', views.registrar_usuario_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login_alt'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('api/status/', api_status.api_status_check, name='api_status_check'),
]
