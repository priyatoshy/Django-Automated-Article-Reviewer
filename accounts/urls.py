from django.urls import path 
from . import views
#imporing path 
#import views file from its own directory

#creating an url configuration/URLConf


urlpatterns = [
    path('',views.login,name='login'),
    path('registration',views.registration,name='registration'),
    path('logout',views.logout,name='logout'),
    path('userarticle',views.userarticle,name='logout')
    
]


