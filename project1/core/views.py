from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def core(request):
    #return HttpResponse("Main tasks page")
    return render(request, 'core/core.html')
