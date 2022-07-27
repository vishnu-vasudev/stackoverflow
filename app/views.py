from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question,User
from .serializer import QuestionSerializer
import requests
import json
from django.core.paginator import Paginator



def display(request):
    return render(request, 'display.html')

class QuestionAPI(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def latest(request):
    res = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
    json_object = res.json()
    for item in json_object['items']:
        question = item['title']
        views = item['view_count']
        tags = item['tags']
        obj = Question(question = question, views = views, tags = tags)
        obj.save()
    data = Question.objects.all()
    return render(request, 'home.html', {'data':data})

def user_login(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            log = User.objects.get(username = username, password = password)
            request.session['user_id'] =log.id     
            return redirect('display')
        except:
            msg = 'Invalid data'
    return render(request, 'user-login.html', {'msg':msg})

def search(request):
    message = ''
    search = request.GET['search']
    if search == '':
        return render(request, 'display.html')
    else:
        resp = requests.get("https://api.stackexchange.com/2.3/search?order=desc&sort=activity&intitle="+ search + "&site=stackoverflow")
        jsonObject = resp.json()
        return render(request, 'display.html', {'obj':jsonObject['items']})
        