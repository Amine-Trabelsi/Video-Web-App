from django.urls import path
from . import views


urlpatterns = [
    path('videos/', views.VideoList.as_view(), name='video-list'),
    path('videos/<int:pk>/', views.VideoDetail.as_view(), name='video-detail'),
]
