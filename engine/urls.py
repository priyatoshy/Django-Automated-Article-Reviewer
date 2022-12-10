from django.urls import path 
from .views import Home,Article,NewArticle,MyArticle,AlterArticle,DeleteArticle

#imporing path 
#import views file from its own directory

#creating an url configuration/URLConf


urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('new-article',NewArticle.as_view(),name="article"),
    path('my-article/<str:pk>',MyArticle.as_view(),name="my-article"),
    path('alter-article/<str:pk>',AlterArticle.as_view(),name="alter-article"),
       path('delete-article/<str:pk>',DeleteArticle.as_view(),name="delete-article"),
    #path('article/<str:pk>')
    
]

