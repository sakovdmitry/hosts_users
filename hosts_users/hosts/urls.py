from django.urls import path

from . import views

app_name = 'hosts'

urlpatterns = [
    path('', views.index, name='index'),
    path('hosts_create', views.hosts_create, name='hosts_create'),
    path('hosts/<int:hosts_id>/edit/', views.hosts_edit, name='hosts_edit'),
]
