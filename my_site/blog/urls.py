from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("article/<article_id>", views.article, name="article_page"),
    path("post/", views.post_article, name="post_article"),
    path("trending/", views.trending, name="trending_articles"),
    path("about/", views.about, name="about_us"),
    path("account/", views.account, name="account"),
    path("login/", views.login_or_signup, name="login_or_signup"),
    path("@<str:author>/", views.author, name="author_page")
]
