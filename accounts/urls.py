from django.urls import path 
from . import views
#imporing path 
#import views file from its own directory

#creating an url configuration/URLConf


urlpatterns = [
    path('login',views.loginUser,name='login'),

    path('logout',views.logoutUser,name='logout'),

    path('register',views.registerUser,name='register'),

    path('show-profile/<str:pk>',views.show_profile,name='show-profile'),
    
    path('update-profile/<str:pk>',views.update_profile,name='update-profile'),


]


