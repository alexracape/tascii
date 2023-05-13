from django.urls import path
from feed import views



urlpatterns = [
    path('', views.feed, name='feed'),
    path('sort=<str:sort>/', views.feed, name='feed'),
    path("view<int:pk>/", views.post_details, name="post_details"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path('post/accept/<int:pk>/', views.post_accept, name='post_accept'),
    path('profile/', views.profile, name='profile'),
    path("post/edit<int:pk>/", views.edit_post, name="edit_post"),
    path('post/delete/<int:pk>/', views.delete_post, name="delete_post"),
    path("make-post/", views.make_post, name="make_post"),
    path('logout/', views.logout_request, name='logout'),
    path('make_review/<int:user_id>/', views.make_review, name='make_review'),
]
