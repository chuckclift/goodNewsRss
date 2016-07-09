from django.shortcuts import render
from django.http import HttpResponse 
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.core.urlresolvers import reverse

from .models import Article, Article_Rating

from nltk.stem import WordNetLemmatizer

def index(request):
    article_list = Article.objects.order_by("-pub_date")[:20]
    fixed_titles = ["_".join(a.title.split()) for a in article_list]
    context = {"article_list": zip(article_list, fixed_titles)} 
    return render(request, "frontpage/index.html", context)

def like(request, title):
    if not request.user.is_authenticated():
        return HttpResponseForbidden()

    wnl = WordNetLemmatizer()
    lemmatized_headline = " ".join([wnl.lemmatize(a) for a in title.split()]) 

    rating = Article_Rating.objects.create(user=request.user.username, 
                                          title=lemmatized_headline, 
                                          rating=1)
    rating.save()
    return HttpResponseRedirect('/')

def dislike(request, title):
    if not request.user.is_authenticated():
        return HttpResponseForbidden()

    wnl = WordNetLemmatizer()
    lemmatized_headline = " ".join([wnl.lemmatize(a) for a in title.split()]) 

    rating = Article_Rating.objects.create(user=request.user.username, 
                                           title=lemmatized_headline,   
                                           rating=0)
    rating.save()
    return HttpResponseRedirect('/')


