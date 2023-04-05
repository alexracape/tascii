from django.urls import path
from feed import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path("<int:pk>/", views.post_details, name="post_details"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
]
