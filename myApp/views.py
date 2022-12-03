from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World<h1>")



def html_page(request):
    data = {
        'title': 'first page',
        'techs': ['html', 'css', 'python', 'django'],
        'technologies': {
            'web': ['html', 'css', 'javascript'],
            'language': ['python', 'django'],
            'tools': ['vs code', 'xampp'],
        }
    }
    return render(request, "index.html", data)

def add_record(request):
    print(request.POST['email'])
    # ORM - object relational mapping
    # Master.objects.create(Email = request.POST['email'], Password=request.POST['password'])

    master = Master()
    master.Email = request.POST['email']
    master.Password = request.POST['password']
    master.save()

    return redirect(html_page)
