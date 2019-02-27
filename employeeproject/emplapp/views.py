from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeApplication

# Create your views here.

def index(request):
    return HttpResponse("working on me")


def Employee(request):

    newForm = EmployeeApplication()

    context = {
        "newForm": newForm
    }

    return render(request, "emplapp/index.html", context)

