from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home-page"),
    path("post/<slug:post_id>", views.post, name="single-post"),
    path("categories", views.categories, name="article-categories"),
    path("create", views.new_post, name="new-post"),
    path("trending", views.trending_posts, name="trending-posts"),
    path("favourites", views.favourite_posts, name="favourite-posts"),

]