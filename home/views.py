from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario


# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        return HttpResponse('aqui')
