from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects, name='allProjects'),
    path('add/', views.add_project, name='add_project'),
    path('<int:id>/', views.delete_project, name='delete_project'),
]
