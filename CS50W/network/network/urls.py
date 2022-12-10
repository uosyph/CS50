from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("follow/<int:user_to_follow>", views.follow, name="follow"),
    path("unfollow/<int:user_to_unfollow>", views.unfollow, name="unfollow"),
    path("following", views.following, name="following"),
    path("newpost", views.new_post, name="newpost"),
    path("editpost/<int:post_id>", views.edit_post, name="editpost"),
    path("updatelike/<int:post_id>", views.update_like, name="updatelike")
]
