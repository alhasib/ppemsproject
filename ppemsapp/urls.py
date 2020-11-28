from .views import * 
from django.urls import path

urlpatterns = [
    path('', my_todolist, name='my_todolist'),
    path('all', all, name='all'),
    path('add-employee', add_employee, name='add_employee'),
    path('login', user_login, name='user-login'),
    path('add-daily-task', add_daily_report, name='add_task'),
    path('leave-form', leave_form, name='leave_form'),
    path('applications', applications, name = 'applications'),
    path('application-evaluation/<status>/<id>', application_evaluation, name = 'application_evaluation'),
    path('my-leave', my_leave_report, name="my_leave"),
    path('move-todo-list/<id>/<sts>', move_todo_list, name="move_todo_list"),
    path('add-to-list', add_to_list, name = "add-to-list"),
    path('my-profile', my_profile, name='my_profile'),
    path('team-profile', team_profile, name='team-profile')
]
