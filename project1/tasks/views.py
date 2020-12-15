from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import Task
from tasks.forms import ADD_TASKFORM, EDIT_TASKFORM, SHOW_HIDE
from django.contrib.auth.decorators import login_required
from django.apps import apps
from django.contrib.auth.models import User
UserProfile = apps.get_model('core', 'UserProfile')
import pdb

# Create your views here.
@login_required(login_url='/login/')
def tasks(request):
    show_hide = SHOW_HIDE()
    if (not Task.objects.filter(user=request.user)):
        return render(request, 'tasks/tasks.html')
        if (request.method == "POST"):
            user_profile = UserProfile.objects.filter(user=request.user).get()
            if(user_profile.tasks_view_hide_completed == 'False'):
                task_objects = Task.objects.filter(user=request.user)
                con = {'task_objects': task_objects, "SHOW_HIDE" : show_hide}
                return render(request, 'tasks/tasks.html', con)
                user_profile.tasks_view_hide_completed = 'True'
            else:
                task_objects = Task.objects.filter(user=request.user, completed='No')
                con = {'task_objects': task_objects, "SHOW_HIDE" : show_hide}
                return render(request, 'tasks/tasks.html', con)
                user_profile.tasks_view_hide_completed = 'False'

    else:
        task_objects = Task.objects.filter(user=request.user)
        con = {'task_objects': task_objects, "SHOW_HIDE" : show_hide}
        return render(request, 'tasks/tasks.html', con)

@login_required(login_url='/login/')
def add_tasks(request):
    if (request.method == "POST"):
        add_taskform = ADD_TASKFORM(request.POST)
        if (add_taskform.is_valid()):
            task = add_taskform.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("/tasks")
        else:
            # Form invalid, print errors to console
            page_data = { "ADD_TASKFORM": add_taskform }
            return render(request, 'tasks/add_tasks.html', page_data)

    else:
        add_taskform = ADD_TASKFORM()
        page_data = { "ADD_TASKFORM": add_taskform }
        return render(request, 'tasks/add_tasks.html', page_data)

@login_required(login_url='/login/')
def edit_tasks(request, pk):
    hh = Task.objects.get(id=pk)
    edit_taskform = EDIT_TASKFORM(instance = hh)

    if (request.method == "POST"):
        edit_taskform = EDIT_TASKFORM(request.POST, instance = hh)

        if (edit_taskform.is_valid()):
            task = edit_taskform.save(commit=False)
            task.user = request.user
            task.id = pk
            task.save()
            return redirect("/tasks")

        else:
            # Form invalid, print errors to console
            page_data = { "EDIT_TASKFORM": edit_taskform }
            return render(request, 'tasks/edit_tasks.html', page_data)

    else:

        page_data = { "EDIT_TASKFORM": edit_taskform }
        return render(request, 'tasks/edit_tasks.html', page_data)

@login_required(login_url='/login/')
def delete(request, pk):
    dele = Task.objects.get(id=pk)
    dele.delete()
    return redirect("/tasks")


@login_required(login_url='/login/')
def toggle(request, pk):
    tt = Task.objects.get(id=pk)

    if(tt.completed == 'Yes'):
        tt.completed = 'No'
    else:
        tt.completed = 'Yes'
    tt.save()
    return redirect("/tasks")
