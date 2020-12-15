from django.shortcuts import render, redirect
from journal.forms import ADD_JOURNALFORM, EDIT_JOURNALFORM
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from journal.models import Journal

# Create your views here.


@login_required(login_url='/login/')
def journal(request):
    if (not Journal.objects.filter(user=request.user)):
        return render(request, 'journal/journal.html')

    else:
        journal_objects = Journal.objects.filter(user=request.user)
        context = {'journal_objects' : journal_objects}
        return render(request, 'journal/journal.html', context)

@login_required(login_url='/login/')
def add_journal(request):
    if (request.method == "POST"):
        add_journalform = ADD_JOURNALFORM(request.POST)
        if (add_journalform.is_valid()):
            journal = add_journalform.save(commit=False)
            journal.user = request.user
            journal.save()
            return redirect("/journal")
        else:
            # Form invalid, print errors to console
            page_data = { "ADD_JOURNALFORM": add_journalform }
            return render(request, 'tasks/add_journal.html', page_data)

    else:
        add_journalform = ADD_JOURNALFORM()
        page_data = { "ADD_JOURNALFORM": add_journalform }
        return render(request, 'journal/add_journal.html', page_data)

@login_required(login_url='/login/')
def edit_journal(request, pk):
    obj = Journal.objects.get(id=pk)
    edit_journalform = EDIT_JOURNALFORM(instance = obj)

    if (request.method == "POST"):
        edit_journalform = EDIT_JOURNALFORM(request.POST, instance = obj)

        if (edit_journalform.is_valid()):
            journal = edit_journalform.save(commit=False)
            journal.user = request.user
            journal.id = pk
            journal.save()
            return redirect("/journal")

        else:
            page_data = {"EDIT_JOURNALFORM": edit_journalform }
            return render(request, 'journal/edit_journal.html', page_data)

    else:
        page_data = {"EDIT_JOURNALFORM": edit_journalform }
        return render(request, 'journal/edit_journal.html', page_data)

@login_required(login_url='/login/')
def delete(request, pk):
    dele = Journal.objects.get(id=pk)
    dele.delete()
    return redirect("/journal")
