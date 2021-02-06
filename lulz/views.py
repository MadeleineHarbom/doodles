import json
import random

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from lulz.models import Comment

#A view function, or view for short, is a Python function that takes a Web request and returns a Web response

images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg',
          '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg']


#rename...
def random_lulz(request):
    imgage = random.choice(images)
    template = render(request, "index.html", {'image_url': imgage}) #delete image_url
    return HttpResponse(template)


#TODO random lulz

@csrf_exempt
def comic(request, comic_id):
    if request.method == 'POST':
        #called if one is posting a comment
        if request.user.is_authenticated:
            username = request.user.username
            Comment.objects.create(text=request.POST.get('comment_area'), comic_id=comic_id, user=username)
        else:
            Comment.objects.create(text=request.POST.get('comment_area'), comic_id=comic_id, user=request.POST.get("username"))
    comments = Comment.objects.filter(comic_id=comic_id)
    #filter does SQL queries for you
    template = render(request, 'comic.html', {
        #dictionary with all infp required to render page
        'previous_url': reverse('comic', kwargs={'comic_id': comic_id - 1 if comic_id > 0 else len(images) - 1}),
        'next_url': reverse('comic', kwargs={'comic_id': comic_id + 1 if comic_id < len(images) - 1 else 0}),
        'comments': comments,
        'comic_url': images[comic_id]
    })
    #kwargs = key value arguments
    return HttpResponse(template)


@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(random_lulz)
        template = render(request, 'login.html') #it aint pretty
        return HttpResponse(template)
    if request.method == 'POST':
        data = request.POST
        user_name = data.get('user_name')
        password = data.get('password')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect(random_lulz)
        else:
            return HttpResponse(render(request, 'login.html'))


@csrf_exempt
def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(random_lulz)
        template = render(request, 'signup.html')
        return HttpResponse(template)
    elif request.method == 'POST':
        data = request.POST
        user_name = data.get('user_name')
        password = data.get('password1')
        password2 = data.get('password2')
        #check that the username is unique
        if password == password2:
            user = User.objects.create_user(username=user_name, password=password)
            #create_user saves in db automatically
            login(request, user)
            template = render(request, 'index.html')
            return redirect(random_lulz)
        else:
            template = render(request, 'signup.html')
            return HttpResponse(template)

def logout_view(request):
    logout(request)
    return redirect(random_lulz)
