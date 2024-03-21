from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'pages/login.html')

def login_page(request):
    return render(request, 'pages/login.html')

def registro(request):
    return render(request, 'pages/registro.html')
