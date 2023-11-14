from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentListRequestHandler.as_view(), name='student-list'),
    path('add-student', views.StudentCreateRequestHandler.as_view(), name='add-student'),
]
