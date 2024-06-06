# blog/urls.py

from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('feed', views.feeed, name= 'feed'),
    path('profile/<str:username>/', views.profile_view, name='profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)