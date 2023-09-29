from django.core.mail import send_mail
from .constants import TASK_FIELDS

def send_email_to_user(email_list):
    """
    Utility function for sending emails to the given email list
    @params: List
    """
    send_mail(
        "New Task Assigned",
        "A new task has been assigned to you. Kindly Checked and complete it before due date",
        "no-reply@rdash.com",
        email_list,
        fail_silently=True
    )

def get_user_assigned_tasks(tasks_data,user):
    """
    Fetches all the tasks assigned to the given user
    @params: QuerySet having all the tasks, username
    returns: List of all the tasks assigned to the user
    """

    fields = TASK_FIELDS
    tasks = list()
    for task in tasks_data:
        assignees = task.assignee.split(",")
        if user not in assignees:
            continue
        data = list()
        for field in fields:
            if field == 'due_date':
                data.append(getattr(task,field).date())
            else:
                data.append(getattr(task,field))
        tasks.append(data)
    return tasks

def get_tasks_list(tasks_data):
    """
    Utility function for retrieving the values from the query set of tasks data in the form of list
    @params: QuerySet having all the tasks
    returns: List
    """
    fields = TASK_FIELDS
    tasks = list()
    for task in tasks_data:
        data = list()
        for field in fields:
            if field == 'due_date':
                data.append(getattr(task,field).date())
            else:
                data.append(getattr(task,field))
        tasks.append(data)
    return tasks

def get_user_created_tasks(tasks_data,user):
    """
    Fetches all the tasks that are created by the given user
    @params: QuerySet having all the tasks, username
    returns: List of all the tasks created by the user
    """
    tasks = list()
    fields = TASK_FIELDS
    for task in tasks_data:
        if task.created_by != user:
            continue
        data = list()
        for field in fields:
            if field == 'due_date':
                data.append(getattr(task,field).date())
            else:
                data.append(getattr(task,field))
        tasks.append(data)
    return tasks