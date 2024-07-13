from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, "website/index.html")
    
    def post(self, request):
        return HttpResponse("POST Request")
    
class PageNF(View):
    def get(self, request):
        return render(request, "404.html")