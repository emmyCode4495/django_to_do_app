from django.urls import path as emmyCode
from . import views

urlpatterns = [
    emmyCode('about/',views.about_page,name="about_page"),
    emmyCode('', views.add_task, name="add_task"),
    emmyCode('updateTask/<int:pk>/', views.update_task, name="update_task"),
    emmyCode('deleteTask/<int:pk>/', views.delete_task, name="delete_task")
     
]