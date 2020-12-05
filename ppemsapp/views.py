from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')

def add_employee(request):
    user = request.user
    user = User.objects.get(username = user)
    print(user)
    u = user.groups.filter(name='HR').exists()
    if u:
        if request.method == 'POST':
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']
            role = request.POST['role']
            email = request.POST['email']
            department = request.POST['department']
            print(role)
            print(department)
            user = User.objects.create_user(username = username, password = password, first_name = first_name,
                    last_name = last_name, email = email
            )
            group = Group.objects.get(id = role)
            print(group.name)
            user.groups.add(group)
            user.save()
            department = Department.objects.get(id = department)
            print(department.name)
            Profile.objects.create(user = user, department = department)

            return HttpResponse('Done')
        else:
            form = UserForm()
            context = {'form':form}
            return render(request, 'user_creation_form.html', context)
    else:
        message = "Server Error!"
        context = {'message':message}
        return render(request, 'message.html', context)



def user_login(request):
    if request.method == 'POST':
        # form = UserLoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('/my-profile')

    form = UserLoginForm()
    context = {'form':form}
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def add_daily_report(request):
    if request.method == 'POST':
        form = DailyTaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            user = request.user 
            form.user = user 
            form.save()
            return HttpResponse("successfully added")

    form = DailyTaskForm()
    context = {'form':form}
    return render(request, 'add-task.html', context)


@login_required(login_url='/login')
def leave_form(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user 
            form.save()
            return HttpResponse('Successfully Added')
    form = LeaveForm()
    context = {'form':form}
    return render(request, 'leave_form.html', context)

@login_required(login_url='/login')
def applications(request):
    if request.user.groups.filter(name = "HR").exists():
        try:
            applications = Leave.objects.filter(checked_in = False)
            if applications:

                context = {'applications':applications}
                return render(request, 'application.html', context)
            else:
                message = "No Applications Is Available"
                context = {'message':message}
                return render(request, 'application.html', context)

        except:
            message = "No Applications Is Available"
            context = {'message':message}
            return render(request, 'application.html', context)
    else:
        message = "Server Error!"
        context = {'message':message}
        return render(request, 'message.html', context)

@login_required(login_url='/login')
def application_evaluation(request, status, id):
    application = Leave.objects.get(id = id)
    application.status = status
    application.checked_in = 1
    application.save()
    return HttpResponse("ok")

@login_required(login_url='/login')
def my_leave_report(request):
    if request.user.is_authenticated:
        my_application = Leave.objects.filter(user = request.user)
        context = {"my_application":my_application}
        return render(request, 'my_application.html', context)
    else:
        return redirect("/login")

def all(request):
    return render(request, 'all.html')

@login_required(login_url='/login')
def my_todolist(request):
    print("myto do list")

    if request.user.is_authenticated:
        user = request.user
        pending_todo_list = TodoList.objects.filter(user = user, pending_status = True)
        working_todo_list = TodoList.objects.filter(user = user, working_status = True)
        done_todo_list = TodoList.objects.filter(user = user, done_status = True)

        context = {'pending_todo_list':pending_todo_list, 'working_todo_list':working_todo_list,
            'done_todo_list':done_todo_list
            }
        return render(request, 'my_todo_list.html', context)
    else:
        return redirect('/login')

@login_required(login_url='/login')
def move_todo_list(request,id,sts):

    to_do_list = TodoList.objects.get(id = id)
    if sts == 'done':
        to_do_list.done_status = True
        to_do_list.working_status = False
        to_do_list.pending_status = False
        to_do_list.save()
        return redirect('/my-todolist')
    elif sts == 'working':
        to_do_list.working_status = True
        to_do_list.pending_status = False 
        to_do_list.done_status = False
        to_do_list.save()
        return redirect('/my-todolist')

@login_required(login_url='/login')
def add_to_list(request):
    if request.method == 'POST':
        what_to = request.POST['what-to-do']
        when_to = request.POST['when-to-do']
        create_todo_list = TodoList.objects.create(user = request.user, what_to_do = what_to,
            when_to_do = when_to
        )
        messages.success(request, 'Added To Do List Successfully')
        return redirect('/my-todolist')


@login_required(login_url='/login')
def my_profile(request):
    if request.user.is_authenticated:

        try:
            user = request.user 
            print(user)
            if user:
                profile = Profile.objects.get(user = user)
                context = {'profile':profile}
                print('asdeeu')
                return render(request, 'profile.html', context)
        except:
            message = "user is not logged in"
            context = {'message':message}
            return render(request, 'profile.html', context)
    else:
        return redirect("/login")

@login_required(login_url='/login')
def team_profile(request):
    try:
        user = request.user 
        print(user)
        if user:
            profile = Profile.objects.get(user = user)
            print(profile.user.username)
            department = profile.department
            all_profile = Profile.objects.filter(department = department)
            print(all_profile)
            context = {'all_profile':all_profile}
            print(context)
            print(3456)
            return render(request, 'team_profile.html', context)
    except:
        message = "user is not logged in"
        context = {'message':message}
        return render(request, 'team_profile.html', context)

def edit_profile(request):
    print("this is eidt view")
    if request.user.is_authenticated:
        if request.method == "POST":
            print("post request")
            profile = Profile.objects.get(user = request.user)
            profile_image = request.POST['profile_image']
            profile.profile_image = profile_image
            profile.save()
            return HttpResponse("ok")
            # user = User.objects.get(username = request.user.username)

        else:
            print("first else block")
            profile = Profile.objects.get(user = request.user)
            print(profile)
            # print(user)
            form = ProfileForm(instance=profile)
            print(form)
            context = {'form':form}
            return render(request, 'edit_profile.html', context)
    else:
        print("else block")
        return redirect('/login')