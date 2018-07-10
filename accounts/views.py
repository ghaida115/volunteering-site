from django.shortcuts import render
from django.http import HttpResponse

from models import institute
from models import comments
from models import volunteer_work

def index(request):
     return render (request, "accounts/index.html" )

def add_institute (request):
    name = institute.objects.create
    context = {"institute": institute}
    return render (request, "accounts/institute.html" ,context)

def edit_institute (request, institute_id):
    name = institute.objects.get(pk = institute_id)
    context = {"institute": institute}
    return render (request, "accounts/institute.html" ,context)

def delete_institute (request):
    name = institute.objects.delete
    context = {"institute": institute}
    return render (request, "accounts/institute.html" ,context)

def add_comment(request):
    text = request.POST['text']
    author = request.POST['author']

def edit_comment(request):
    text = request.POST['text']
    author = request.POST['author']

def delete_comment(request):
    text = request.POST['text']
    author = request.POST['author']

def add_volunteer_work(request) :
    name = volunteer_work.objects.create
    context = {"volunteer_work":volunteer_work}
    return render (request, "accounts/volunteer_work.html" ,context)

def edit_volunteer_work(request, volunteer_work_id) :
    name = volunteer_work.objects.get(pk = volunteer_work_id)
    context = {"volunteer_work":volunteer_work}
    return render (request, "accounts/volunteer_work.html" ,context)

def delete_volunteer_work(request) :
    name = volunteer_work.objects.delete
    context = {"volunteer_work":volunteer_work}
    return render (request, "accounts/volunteer_work.html" ,context)

def show (request, institute_id):
    article = show.objects.get(pk = institute_id)
    context = {"institute": institute}
    return render (request, "accounts/show.html" ,context)
