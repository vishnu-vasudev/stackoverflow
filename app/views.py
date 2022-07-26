from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question,User
from .serializer import QuestionSerializer
import requests
import json



def index(request):
    return render(request, 'index.html')

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

def user_reg(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            log = User.objects.get(username = username, password = password)
            request.session['user_id'] =log.id     
            return redirect('index')
        except:
            msg = 'Invalid data'
    return render(request, 'user-reg.html', {'msg':msg})

def check(request):
    dat=[]
    c=0
    msg=''
    if request.method == 'POST':
        search = request.POST['search']
        resp = requests.get("https://api.stackexchange.com/2.3/search?order=desc&sort=activity&intitle=Search&site=stackoverflow")
        jsonObject = resp.json()
        return render(request, 'index.html', {'obj':jsonObject})

        # ob = Question.objects.all()
        # for i in ob:
        #     c=1
        #     qtn = i.question.split()
        #     if search in qtn:
        #         dat.append(i.question)
        # if c == 0:
        #     print('hi')
        #     msg = "No data"
        #     return render('index.html', {'msg':msg})
        # else:
            
        #     return render('index.html', {'dat':dat})