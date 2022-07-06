from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
      'logout/',
      LogoutView.as_view(template_name='logged_out.html'),
      name='logout'
    ),
]
