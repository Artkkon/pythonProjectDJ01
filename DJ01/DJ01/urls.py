
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('index/', include('main.urls')),
    path('about/', include('main.urls')),
    path('gallery/', include('main.urls')),
    path('contact/', include('main.urls')),
]
