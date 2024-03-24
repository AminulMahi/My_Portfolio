from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('login_user/', views.login_user, name='login_user'),
    path('autolog_out/', views.autolog_out, name='autolog_out'),
]