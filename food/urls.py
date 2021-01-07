from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from food import views

urlpatterns = [
    path('profile/', views.ProfileList.as_view()),
    path('profile/<int:pk>/', views.ProfileDetail.as_view()),
    path('skill/', views.SkillList.as_view()),
    path('skill/<int:pk>/', views.SkillDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)