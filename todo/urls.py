from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list,name="todo_list"),
    path('create', views.create_todo,name="create_todo"),
    path('complete/<int:todo_id>', views.complete_todo,name="complete_todo"),
    path('delete/<int:todo_id>', views.delete_todo,name="delete_todo"),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout_view,name='logout')
]