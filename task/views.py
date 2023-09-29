from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentication.models import User
from .utils import get_tasks_list, get_user_assigned_tasks, get_user_created_tasks, send_email_to_user
from django.contrib import messages
from .constants import TASK_COLUMNS, TASK_FIELDS
from .models import Task

# Create your views here.

@login_required
def task_page(request):
    assigned_to = request.GET.get("assigned_to")
    created_by = request.GET.get("created_by")
    due_date = request.GET.get("due_date")
    username = request.user.username.capitalize()

    users = User.objects.values_list("username", flat = True)

    data = {}

    if created_by not in ["",None] or assigned_to not in ["", None] or due_date not in ["", None]:

        query = {}
        
        if created_by != "":
            query['created_by'] = created_by

        if due_date != "":
            query['due_date__lte'] = due_date

        tasks_data = Task.objects.filter(**query)

        if assigned_to not in ["", None]:
            tasks = get_user_assigned_tasks(tasks_data, assigned_to)
        else:
            tasks = get_tasks_list(tasks_data)

        data = {
            "tasks" : tasks,
            "fields" : TASK_COLUMNS,
            "users" : users,
            "username": username,
            "assigned_to": assigned_to,
            "created_by": created_by,
            "due_date": due_date
        }

    else:
        data = {
            "users" : users,
            "username": username
        }

    return render(request,"task_page.html", data)

@login_required
def create_task(request):
    user_list = User.objects.values_list('username', flat=True)
    users = list()

    for user in user_list:
        users.append(user)

    return render(request, "create_task.html", {
        "users": users
    })

def save_task(request):
    try:
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        assignee_list = request.POST.getlist('assignee')
        created_by = request.user.username

        assignee = ",".join([assignee for assignee in assignee_list if assignee != ""])

        new_task = Task(
            title = title,
            description = description,
            due_date = due_date,
            assignee = assignee,
            created_by=created_by
        )

        new_task.save()

        assignee_list = assignee.split(",")
        email_data = User.objects.filter(username__in = assignee_list)

        email_list = [email.email_id for email in email_data]
        send_email_to_user(email_list)
        messages.success(request, "Task Created Successfully")
        return redirect('')
    
    except:
        messages.error(request, "Some Error Occurred while creating the tasks")
        return redirect('/tasks')
    
@login_required
def user_tasks(request):

    user = request.user.username

    tasks = Task.objects.all()
    assigned_tasks = get_user_assigned_tasks(tasks, user)
    created_tasks = get_user_created_tasks(tasks,user)

    data = {
        "assigned_tasks": assigned_tasks,
        "created_tasks": created_tasks,
        "fields" : TASK_COLUMNS
    }

    return render(request, 'user_tasks.html', data)