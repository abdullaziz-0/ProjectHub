from . import views
from django.urls import path,include

urlpatterns=[

path('',views.login,name='home')

]
