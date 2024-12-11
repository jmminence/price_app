from django.contrib import admin
from django.urls import path, include
from autenticacion.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacion/', include('autenticacion.urls')),
    path('', home, name='home'),  # Ruta para la página de inicio
]