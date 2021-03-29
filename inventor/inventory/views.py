from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Engin

# Create your views here.
def index(request):
    engins = Engin.objects.all()
    return render(request, "inventory/index.html", {
        "engins": engins
    })
    
def engins(request, engin_id):
    eng_id = Engin.objects.get(id=engin_id)
    return render(request, "inventory/engins.html", {
        "eng_id": eng_id
    })
