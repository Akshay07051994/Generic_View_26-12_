from django.urls import path
from .views import StudentAPI, StudentDetailAPI

urlpatterns = [
    path('stu/', StudentAPI.as_view()),
    path('stu/<int:pk>/', StudentDetailAPI.as_view())
]