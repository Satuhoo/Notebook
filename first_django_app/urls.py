from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('notebook/', include('notebook.urls')),
    path('admin/', admin.site.urls),
]
