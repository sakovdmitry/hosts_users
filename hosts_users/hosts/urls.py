from django.urls import path

from . import views

app_name = 'hosts'

urlpatterns = [
    path('', views.index, name='index')
]
