from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def post(request, post_id):
    return HttpResponse(f"Viewing Post Page - {post_id}")

def categories(request):
    return HttpResponse("Viewing Page - Categories")

def new_post(request):
    return HttpResponse("Viewing Page - New Post")

def trending_posts(request):
    return HttpResponse("Viewing Page - trending_posts")

def favourite_posts(request):
    return HttpResponse("Viewing Page - favourite_posts")