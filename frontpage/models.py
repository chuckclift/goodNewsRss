from django.db import models


class Source(models.Model):
    url = models.CharField(max_length=300)
 
class Article(models.Model):
    source_id = models.IntegerField(default=0) 
    url = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField('Date Published')

