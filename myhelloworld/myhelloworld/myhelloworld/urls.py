from django.contrib import admin
from django.urls import path, include
from hello import views  # Import views from the "hello" app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello_world, name='hello_world'),  # Define the URL pattern for the root path
]
