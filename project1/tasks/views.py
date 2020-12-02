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
            page_data = { "add_taskform": add_taskform }
            return render(request, 'tasks/tasks.html', page_data)

    else:
        add_taskform = ADD_TASKFORM()
        page_data = { "ADD_TASKFORM": add_taskform }
        return render(request, 'tasks/add_tasks.html', page_data)

def edit_tasks(request):
    if (request.method == "POST"):
        edit_taskform = EDIT_TASKFORM(request.POST);

        if (edit_tasks.is_valid()):
            id = edit_taskform["id"]
            description = edit_taskform.cleaned_data["description"]
            catagory = chess_form.cleaned_data["catagory"]
            hh = Board.objects.get(id=id)
            vall = hh.value
            Board(description=description, catagory=catagory).save()
            Board(name=location, value=" ").save()
            return redirect("/tasks")
        else:
            page_data = { "edit_taskform": edit_taskform }
            return render(request, 'tasks/edit_tasks.html', page_data)

    else:
        edit_taskform = EDIT_TASKFORM()
        page_data = { "Edit_TASKFORM": edit_taskform }
        return render(request, 'tasks/edit_tasks.html', page_data)

def delete(request):
    dele = Task.objects.get(pk = emp_id)
    dele.delete()
