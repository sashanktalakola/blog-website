from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home-page"),
    path("@<str:user_id>/<slug:slug>", views.post, name="single-post"),
    path("categories", views.categories, name="article-categories"),
    path("category/<slug:category>", views.category_posts, name="posts-category"),
    path("create", views.new_post, name="new-post"),
    path("trending", views.trending_posts, name="trending-posts"),
    path("favourites", views.favourite_posts, name="favourite-posts"),
]