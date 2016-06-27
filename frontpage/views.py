from django.shortcuts import render
from django.http import HttpResponse 
from django.http import HttpResponseRedirect, HttpResponseServerError

from .models import Article, Article_Rating

def index(request):
    article_list = Article.objects.order_by("-pub_date")[:20]
    context = {"article_list": article_list}
    return render(request, "frontpage/index.html", context)

def like(request, title):
    if not request.user.is_authenticated():
        return HttpResponseForbidden()

    username = request.user.username
    rating = Article_Rating.objects.create(user=username, title=title, rating=1)
    rating.save()
    return HttpResponse("You liked " + title)

def dislike(request, title):
    if not request.user.is_authenticated():
        return HttpResponseForbidden()

    username = request.user.username
    rating = Article_Rating.objects.create(user=username, title=title, rating=-1)
    rating.save()
    return HttpResponse("You disliked " + title)






