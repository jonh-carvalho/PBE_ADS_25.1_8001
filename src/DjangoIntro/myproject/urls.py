from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('api/', include('myapp.api_urls')),  # URLs da API
    path('api-auth/', include('rest_framework.urls')),  # Login para a API
]
