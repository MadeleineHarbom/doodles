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


#images = ['0.jpg', '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg',
#       '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg']

images = {'0': 'Just a little...', '1': 'Working station', '2': 'Keep distance',
          '3': 'Priotities', '4': 'How to avoid stress', '5': 'Keeping up apperances',
          '6': 'Date night', '7': 'Hobbies', '8':'Loniness',
          '9': 'Impossible problems', '10': 'Pre meeting', '11': 'D&D',
          '12': 'Risk analysis', '13': 'Hostile workenviroment', '14': 'Happy New Year',
          '15': 'Dressing up', '16': 'When you\'re to shy to talk to peple'}

#rename...
def random_lulz(request):
    #imgage = random.choice(images)
    template = render(request, "index.html", {'comics': images})
    return HttpResponse(template)


#TODO random lulz
def randomized_comic(request):
    imgage = random.choice(images)

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
        'comic_id': comic_id,
        'name': images[str(comic_id)]
    })
    #kwargs = key value arguments
    return HttpResponse(template)


@csrf_exempt
def login_view(request):
    if request.method == 'GET':
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
            return HttpResponse(render(request, 'login.html', {'error': 'Invalid username or password'}))


@csrf_exempt
def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            template = render(request, 'signup.html', {'error': 'You are already logged in'})
            return HttpResponse(template)
        else:
            template = render(request, 'signup.html')
            return HttpResponse(template)
    elif request.method == 'POST':
        data = request.POST
        user_name = data.get('user_name')
        password = data.get('password1')
        password2 = data.get('password2')
        #check that the username is unique
        try :
            User.objects.get(username=user_name)
            template = render(request, 'signup.html', {'error': 'Username already in use'})
            return HttpResponse(template)
        except:
            if password == password2:
                user = User.objects.create_user(username=user_name, password=password)
                #create_user saves in db automatically
                login(request, user)
                template = render(request, 'index.html')
                return redirect(random_lulz)
            else:
                template = render(request, 'signup.html', {'error': 'Passwords did not match'})
                return HttpResponse(template)

def logout_view(request):
    logout(request)
    return redirect(random_lulz)
