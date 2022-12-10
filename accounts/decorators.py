from django.http import HttpResponse
from django.shortcuts import redirect


def unauthneticated_user(view_func):

    def wrapper(request,*args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect('login')
        else:
            return view_func(request,*args, **kwargs)

    return wrapper

