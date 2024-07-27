
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('scanner.urls')),
    path('scan',include('scanner.urls')),
    # path('login',include('scanner.urls')),

]