from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('tasks/', include('tasks.urls')),  # Add this line
]
