from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login



# Create your views her

#vista del index

def index (request):
    return render(request, "index.html")
#vista del login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Cambia 'index' por la URL que quieras redirigir después del login
        else:
            messages.error(request, 'Usuario o contraseña incorrecta.')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, '¡Registro exitoso! Te has registrado correctamente.')
            return redirect('index')
        else:
            messages.error(request, '¡Error de registro! Por favor, corrige los errores a continuación.')
            context = {'form': form}
            return render(request, 'registro.html', context)
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registro.html', context)
    