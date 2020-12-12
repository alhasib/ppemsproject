from .views import * 
from django.urls import path
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('', my_todolist, name='my_todolist'),
    path('menus', menu, name='menu'),
    path('email-sending', email_sending, name='email_sending'),
    path('forget-password', forget_password, name='forget_password'),
    path('search-profile', search_profile, name='search_profile'),
    

    path('change-password', change_passaword, name='change_passaword'),




    # path('abc', abc, name='abc'),

    path('accounts/reset_password', auth_view.PasswordResetView.as_view(), name = 'password_reset'),
    path('reset_password_sent', auth_view.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset_password_complete',auth_view.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),


    path('all', all, name='all'),
    path('add-employee', add_employee, name='add_employee'),
    path('edit-profile', edit_profile, name='edit_profile'),
    path('login', user_login, name='user-login'),
    path('logout', user_logout, name='user_logout'),
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
