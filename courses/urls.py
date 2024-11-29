from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('course_list/', views.course_list, name='course_list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
