"""
Definition of urls for Cestabasica.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms,views
from app.views import (
    cliente_form,
    produto_form,
    cesta_form,
   )

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),

    path('cliente/',views.lista_cliente, name='cliente'),

    path('cliente/edit/<int:cpf>/',views.cliente_update, name='cliente_update'),

    path('cliente/delete/<int:cpf>/',views.cliente_delete, name='cliente_delete'),

    path('cliente/criarcliente/',views.cliente_form, name='cadastrar_cliente'),

    path('produto/',views.lista_produto, name='produto'),

    path('produto/edit/<int:codigo_barras>/',views.produto_update, name='produto_update'),

    path('produto/criarproduto/',views.produto_form, name='cadastrar_produto'),

    path('delete/<int:codigo_barras>', views.produto_delete, name='produto_delete'),

    path('cesta/criarcesta/', views.cesta_form, name='cadastrar_cesta'),

    path('cesta/', views.lista_cesta, name='cesta'),

]
