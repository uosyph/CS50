from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("category", views.showCat, name="category"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("addToWatchlist/<int:id>", views.addToWatchlist, name="addToWatchlist"),
    path("removeFromWatchlist/<int:id>", views.removeFromWatchlist,
         name="removeFromWatchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("addComment/<int:id>", views.addComment, name="addComment"),
    path("addBid/<int:id>", views.addBid, name="addBid"),
    path("endAuction/<int:id>", views.endAuction, name="endAuction"),
]
