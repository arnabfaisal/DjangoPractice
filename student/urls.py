from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView, name='home'),
    path('registration/', views.StudentRegistrationView.as_view(), name='student_registration'),
    path('profile/<int:id>', views.studentProfile, name='student_profile'),
    path('update/<int:pk>', views.StudentUpdateView.as_view(), name='student_update'),
    path('delete/<int:id>', views.studentDelete, name='student_delete'),
]
