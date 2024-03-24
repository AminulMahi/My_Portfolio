from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('admin_blog/', views.admin_blog, name='admin_blog'),
    path('insert_blog', views.insert_blog, name='insert_blog'),
    path('delete_blog/<str:id>', views.delete_blog, name='delete_blog'),
    path('signup/', views.signup, name='signup')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
