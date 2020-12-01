from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def budget(request):
    #return HttpResponse("Main tasks page")
    return render(request, 'budget/budget.html')
