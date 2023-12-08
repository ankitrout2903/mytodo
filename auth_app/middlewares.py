from django.shortcuts import render,redirect

#*******Authenticated********

def auth(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        else:
            return view_function(request,*args,**kwargs)
    return wrapped_view


#*******UnAuthenticated********
def guest(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_function(request,*args,**kwargs)
    return wrapped_view