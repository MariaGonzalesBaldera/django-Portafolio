from .views import AddProject, ListProject

from django.urls import path
urlpatterns =[
    path('add/', AddProject.as_view(),name='AddProject'),
    path('', ListProject.as_view()),
]