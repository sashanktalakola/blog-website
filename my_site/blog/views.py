from django.shortcuts import render
from django.http import HttpResponse
from .recommendations import *


# Create your views here.
def index(request):
    page_data = {}
    page_data["login"] = {}

    page_data["NUM_SUB_RECOMMENDATIONS"] = NUM_SUB_RECOMMENDATIONS

    page_data["login"]["logged_in"] = False
    page_data["login"]["name"] = "Sashank Talakola"

    page_data["hero_section"] = getMainRecommendation()
    sub_recommendations = getSubRecommendation()
    page_data["main_sub_recommendation"] = sub_recommendations[0]
    page_data["rem_sub_recommendation"] = sub_recommendations[1:]
    page_data["all_stories"] = getAllStoriesRecommendation()
    page_data["popular_stories"] = getPopularStoriesRecommendations()

    return render(request, "blog/index.html", {"page_data": page_data})


def article(request, article_id):
    return HttpResponse("Article Page")

def post_article(request):
    return HttpResponse("Post Article Page")

def trending(request):
    return HttpResponse("Trending Articles Page")

def about(request):
    return HttpResponse("About Us Page")

def account(request):
    return HttpResponse("IDK Page")

def login_or_signup(request):
    return HttpResponse("Login / Signup Page")

def author(request, author):
    return HttpResponse("Author Page" + author)