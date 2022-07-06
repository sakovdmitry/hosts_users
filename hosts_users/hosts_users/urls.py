from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('hosts.urls', namespace='hosts')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
