from django.urls import path
from . import views
urlpatterns = [
    path("", views.feed, name="feed"),
    path("register/", views.register, name="register"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("post/create/", views.create_post, name="create_post"),
    path("post/<int:post_id>/delete/", views.delete_post, name="delete_post"),
    path("post/<int:post_id>/comment/", views.add_comment, name="add_comment"),
    path("post/<int:post_id>/like/", views.toggle_like, name="toggle_like"),
    path("follow/<str:username>/", views.toggle_follow, name="toggle_follow"),
]
