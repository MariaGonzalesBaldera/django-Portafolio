from .views import registerView, index, AddProject, pro_details,ProjectUpdate,ListPaginacion
from django.contrib.auth.views import LoginView, logout_then_login

from django.urls import path
urlpatterns =[
    path('', index.as_view(),name='index'),
    path('accounts/login/',LoginView.as_view(), name='login'),
    path('register/',registerView.as_view(), name='register'),
    path('logout/',logout_then_login, name='logout'),
    path('porta_details/<int:id>',pro_details , name='porta_details'),
    path('add/', AddProject.as_view(),name='AddProject'),
    path('UpdateProject/<int:pk>', ProjectUpdate.as_view(),name='UpdateProject'),    
    path('ListPaginacion/', ListPaginacion.as_view(),name='ListPaginacion'),    
]