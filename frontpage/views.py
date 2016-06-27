from django.shortcuts import render
from django.http import HttpResponse 

from .models import Article

def index(request):
    article_list = Article.objects.order_by("-pub_date")[:20]
    context = {"article_list": article_list}
    return render(request, "frontpage/index.html", context)

def like(request, title):
    return HttpResponse("Hello, you liked " + title)

def dislike(request, title):
    return HttpResponse("Hello, you disliked " + title)


