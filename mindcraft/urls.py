from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('pages/login.html', views.login_page, name='login_page'),
     path('pages/registro.html', views.registro, name='registro'),
]
