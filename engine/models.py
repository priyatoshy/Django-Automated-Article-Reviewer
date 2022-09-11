from django.db import models

# Create your models here.
class Blog(models.Model):

    title=models.CharField(max_length=100)
    topic=models.CharField(max_length=100)
    content=models.TextField()
    publishedOn=models.DateField(null=True,blank=True)
    
class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    content=models.TextField()
    summary=models.TextField()
    review=models.CharField(max_length=100)

