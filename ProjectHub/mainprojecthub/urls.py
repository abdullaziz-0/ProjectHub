from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainapp.urls')),
    path('login/',include('login.urls')),
    path('signup/',include('signup.urls')),
    path('upload/',include('upload.urls')),
    path('myproject/',include('myproject.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
