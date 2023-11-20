from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as ui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('API/', include('openapi.urls'))
] + ui
