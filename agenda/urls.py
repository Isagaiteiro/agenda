"""
URL configuration for agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app.views import index, create_user, formulario_user, list_users, edit_user, update_user, delete_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('users/create/', create_user, name='criar_usuario'),
    path('users/', list_users, name='listar_usuarios'),
    path('users/<int:pk>/editar', edit_user, name='exibir_usuario'),
    path('users/<int:pk>/atualizar/', update_user, name='atualizar_usuario'),
    path('users/<int:pk>/excluir/', delete_user, name='excluir_usuario'),
    path('users/novo', formulario_user, name='formulario_usuario'),

    
]
