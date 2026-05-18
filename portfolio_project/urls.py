from django.contrib import admin
from django.urls import path
from projects.views import home  # This imports the logic we just wrote

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), # This makes it the main homepage
]