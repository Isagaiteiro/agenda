from django.shortcuts import render, redirect, get_object_or_404, reverse
from app.forms import UsuarioModelForm, TarefaModelForm
from app.models import UsuarioModel, TarefaModel


def index(request):
    return render(request, 'index.html')

def list_users(request):
    usuarios = UsuarioModel.objects.all()
    return render(request, 'list_users.html', {'usuarios': usuarios})

def create_user(request):
    if request.method == 'POST':
        user_form = UsuarioModelForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            usuarios = UsuarioModel.objects.all()
            return render(request, 'list_users.html', {'usuarios': usuarios})
    else:
        user_form = UsuarioModelForm()
        return render(request, 'create_user.html', {'user_form': user_form})
    
def edit_user(request, pk):
    usuarios = UsuarioModel.objects.all()
    if request.method == 'GET':
        user = get_object_or_404(UsuarioModel, pk=pk)
        form = UsuarioModelForm(instance=user)
        return render(request, 'edit_user.html', {'form': form, 'user': user})
    else:
        return render(request, 'list_users.html', {'usuarios': usuarios})

def update_user(request, pk):
    user = get_object_or_404(UsuarioModel, pk=pk)
    if request.method == 'POST':
        form = UsuarioModelForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            usuarios = UsuarioModel.objects.all()  
            return render(request, 'list_users.html', {'usuarios': usuarios})
    else:
        form = UsuarioModelForm(instance=user)
    return render(request, 'update_user.html', {'form': form, 'user': user})

def delete_user(request, pk):
    user = get_object_or_404(UsuarioModel, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('listar_usuarios')
    else:
        usuarios = UsuarioModel.objects.all()
        return render(request, 'list_users.html', {'usuarios': usuarios})

def formulario_user(request):
    form = UsuarioModelForm()
    return render(request, 'create_user.html', {'form': form})




