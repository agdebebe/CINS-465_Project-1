from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.apps import apps
import pdb
Tasks = apps.get_model('tasks', 'Task')
Budget = apps.get_model('budget', 'Budget')
# Create your views here.

@login_required(login_url='/login/')
def core(request):
    tasks_object = Tasks.objects.filter(user=request.user)
    completed_counter = 0
    pending_counter = 0
    for row in tasks_object:
        if(row.completed == 'Yes'):
            completed_counter += 1
        else:
            pending_counter += 1
    budget_object = Budget.objects.filter(user=request.user)
    tow = []
    cow = []
    for row in budget_object:
         tow.append(row.actual)
         cow.append(row.projected)

    context = {'completed' : completed_counter, 'pending' : pending_counter, 'tow' : tow, 'cow' : cow}
    return render(request, 'core/core.html', context)
