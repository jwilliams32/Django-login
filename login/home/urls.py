from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import login, logout


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.update_profile),
    path('accounts/register/', views.register, name='register'),
    path('logout/', logout, {'template_name': 'home/home.html'}),
    path('login/', login, {'template_name': 'home/login.html'}),

    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
]