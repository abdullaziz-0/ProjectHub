from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_projects, name='user_projects'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('project/<int:project_id>/', views.projectName, name='projectName'),
    path('project/<int:project_id>/edit/', views.project_update, name='project_update'),
]
