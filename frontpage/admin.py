from django.contrib import admin

from .models import Article, Source, Article_Rating

admin.site.register(Article)
admin.site.register(Article_Rating)
admin.site.register(Source)
