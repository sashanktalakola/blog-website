from django.http import HttpResponse
from django.shortcuts import render
from . import data

# Create your views here.
def index(request):
    return render(request, "blog/index.html", {
        "main_post": data.main_post,
        "top_posts_row": data.top_posts_row,
        "top_posts_col": data.top_posts_col,
        "all_stories": data.all_stories,
        "popular_stories": data.popular_stories,
        }        
    )

def post(request, user_id, slug):
    return render(request, "blog/single-post.html")
    #return HttpResponse(f"Viewing Post Page - {slug} From User - {user_id}")

def categories(request):
    return HttpResponse("Viewing Page - Categories")

def new_post(request):
    return HttpResponse("Viewing Page - New Post")

def trending_posts(request):
    return HttpResponse("Viewing Page - trending_posts")

def favourite_posts(request):
    return HttpResponse("Viewing Page - favourite_posts")