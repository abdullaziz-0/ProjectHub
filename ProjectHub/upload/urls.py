from . import views
from django.urls import path

urlpatterns=[

path('',views.upload,name='upload')
]

