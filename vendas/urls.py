from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('vendas.core.urls', namespace='core')),
    path('admin/', admin.site.urls),
]
