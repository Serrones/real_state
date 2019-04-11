from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('pages/', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
]
