from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('activity/', views.ActivityList.as_view(), name="main"),
    path('activity/<int:pk>/', views.ActivityDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)