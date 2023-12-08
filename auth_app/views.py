from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from .middlewares import auth,guest
from .models import Todo
# Create your views here.
@guest
def register_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('login')
    else:
        intial_data = {'username':'','password1':'','password2':''}
        form = UserCreationForm(initial=intial_data)
    return render(request,'auth/register.html',{'form':form})
@guest
def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        intial_data = {'username':'','password':''}
        form = AuthenticationForm(initial=intial_data)
    return render(request,'auth/login.html',{'form':form})

@auth
def dashboard(request):
    return render(request,'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')




# Todo  views here.
@auth
def todo_list(request):
    todos = Todo.objects.order_by('-id')
    return render(request, 'dashboard.html',{'todos':todos})


@auth
def create_todo(request):
    if request.method=='POST': 
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title,description=description)

    return redirect('todo_list')

@auth
def complete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

@auth
def delete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
