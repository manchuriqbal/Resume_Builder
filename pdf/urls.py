from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pdf'),
    path('<int:pk>/', views.resume, name='resume'),
    path('list/', views.list, name='list')
]
