from . import views
from django.urls import path,include
from django.contrib.auth.views import LogoutView

urlpatterns=[

path('',views.login,name='login'),
path('logout/', LogoutView.as_view(), name='logout'),

]

