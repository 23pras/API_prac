from django.urls import path

from . import views

urlpatterns = [
    path('', views.personALL, name='person'),
    path('<int:userid>/', views.detail, name='detail'),
    path('hello/', views.hello_world, name='hello_world'),
    path('classapi/', views.ListUsers.as_view(), name='hello_world'),
]