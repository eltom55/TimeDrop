from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('calendar/<str:pk>/', views.CalendarView.as_view(), name="calendar"),
    path('todo/<str:pk>/', views.todo, name="todo"),

    path('addTask/', views.addTask, name="addTask"),
]
