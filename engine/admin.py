from django.contrib import admin

# Register your models here.
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=['topic','writer']
    list_filter=['writer','created_on']
    search_fields=['title']
