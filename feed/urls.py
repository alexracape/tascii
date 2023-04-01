from django.urls import path
from feed import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path("<int:pk>/", views.post_details, name="post_details"),
]