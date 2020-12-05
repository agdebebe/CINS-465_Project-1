from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import Task
from tasks.forms import ADD_TASKFORM, EDIT_TASKFORM
import pdb;

# Create your views here.

def tasks(request):

    task_objects = Task.objects.all()
    con = {'task_objects': task_objects}
    return render(request, 'tasks/tasks.html', con)


def add_tasks(request):
    if (request.method == "POST"):
        add_taskform = ADD_TASKFORM(request.POST)
        if (add_taskform.is_valid()):
            description = add_taskform.save()
            catagory = add_taskform.save()
            return redirect("/tasks")
        else:
            # Form invalid, print errors to console
            page_data = { "ADD_TASKFORM": add_taskform }
            return render(request, 'tasks/tasks.html', page_data)

    else:
        add_taskform = ADD_TASKFORM()
        page_data = { "ADD_TASKFORM": add_taskform }
        return render(request, 'tasks/add_tasks.html', page_data)

def edit_tasks(request, pk):
    hh = Task.objects.get(id=pk)
    edit_taskform = EDIT_TASKFORM(instance = hh)

    if (request.method == "POST"):
        edit_taskform = EDIT_TASKFORM(request.POST, instance = hh)

        if (edit_taskform.is_valid()):
            description = edit_taskform.save()
            catagory = edit_taskform.save()
            return redirect("/tasks")

        else:
            # Form invalid, print errors to console
            page_data = { "EDIT_TASKFORM": edit_taskform }
            return render(request, 'tasks/tasks.html', page_data)

    else:
        hh = Task.objects.get(id=pk)
        edit_taskform = EDIT_TASKFORM(instance = hh)
        page_data = { "EDIT_TASKFORM": edit_taskform }
        return render(request, 'tasks/edit_tasks.html', page_data)

def delete(request, pk):
    dele = Task.objects.get(id=pk)
    page_data = {"Dele": dele}
    return render(request, 'delete.html', page_data)
