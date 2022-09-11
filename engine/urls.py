from django.urls import path 
from . import views
#imporing path 
#import views file from its own directory

#creating an url configuration/URLConf


urlpatterns = [
    path('',views.home,name='home'),
    path('blogs',views.blogs,name='blogs'),
]

