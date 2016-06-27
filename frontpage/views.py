from django.shortcuts import render

from .models import Article

def index(request):
    article_list = Article.objects.order_by("-pub_date")[:20]
    context = {"article_list": article_list}
    return render(request, "frontpage/index.html", context)


