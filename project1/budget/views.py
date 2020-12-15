from django.shortcuts import render, redirect
from django.http import HttpResponse
from budget.models import Budget
from budget.forms import ADD_BUDGETFORM, EDIT_BUDGETFORM
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/login/')
def budget(request):
    if (not Budget.objects.filter(user=request.user)):
        return render(request, 'budget/budget.html')

    else:
        budget_object = Budget.objects.filter(user=request.user)
        surplus = 0
        deficit = 0
        total_proj = 0
        total_act = 0
        for row in budget_object:
            proj = row.projected
            act = row.actual
            total_proj += proj
            total_act += act
        if(total_proj > total_act):
            surplus = total_proj - total_act
        else:
            deficit = total_act - total_proj
        context = {'budget_object' : budget_object, 'surplus' : surplus, 'deficit' : deficit}
        return render(request, 'budget/budget.html', context)


@login_required(login_url='/login/')
def add_budget(request):
    if(request.method == "POST"):
        add_budgetform = ADD_BUDGETFORM(request.POST)

        if(add_budgetform.is_valid()):
            budget = add_budgetform.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect("/budget")
        else:
            page_data = {"ADD_BUDGETFORM" : add_budgetform}
            return render(request, 'budget/budget.html', page_data)

    else:
        add_budgetform = ADD_BUDGETFORM()
        page_data = {"ADD_BUDGETFORM" : add_budgetform}
        return render(request, 'budget/add_budget.html', page_data)

@login_required(login_url='/login/')
def edit_budget(request, pk):
    tt = Budget.objects.get(id=pk)
    edit_budgetform = EDIT_BUDGETFORM(instance = tt)

    if(request.method == "POST"):
        edit_budgetform = EDIT_BUDGETFORM(request.POST, instance = tt)

        if(edit_budgetform.is_valid()):
            budget = edit_budgetform.save(commit=False)
            budget.user = request.user
            budget.id = pk
            budget.save()
            return redirect("/budget")

        else:
            page_data = { "EDIT_BUDGETFORM": edit_budgetform }
            return render(request, 'budget/edit_budget.html', page_data)

    else:
        page_data = { "EDIT_BUDGETFORM": edit_budgetform }
        return render(request, 'budget/edit_budget.html', page_data)

@login_required(login_url='/login/')
def delete(request, pk):
    dele = Budget.objects.get(id=pk)
    dele.delete()
    return redirect("/budget")
