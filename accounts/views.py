from django.shortcuts import render
from django.http import HttpResponse

from models import ?

def index(request):
    return HttpResponse ("الصفحة الرئيسية")

def institute (request, article_id):
    name = .objects.get
    description = {"":}
    return render (request, "/institute.html" ,description)

def comment(request):
    text = request.POST['text']
    author = request.POST['author']
    date =

def volunteer_work(request) :
    name = .objects.get
    description = {"":}
    return render (request, "/volunteer_work.html" ,description)

