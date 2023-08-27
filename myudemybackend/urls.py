from django.contrib import admin
from django.urls import path , include


admin.site.site_header = "Myudemy backend"
admin.site.site_title = "Myudemy backend portal"
admin.site.index_title = "Welcome to Myudemy "




urlpatterns = [
    path('',include("myapp.urls")),
    path('admin/', admin.site.urls),
]
