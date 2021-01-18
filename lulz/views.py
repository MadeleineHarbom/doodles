import json
import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from lulz.models import Comment

images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg',
          '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg']


def random_lulz(request):
    imgage = random.choice(images)
    template = render(request, "index.html", {'image_url': imgage})
    return HttpResponse(template)


@csrf_exempt
def comic(request, comic_id):
    if request.method == 'POST':
        Comment.objects.create(text=request.POST.get('comment_area'), comic_id=comic_id, user=request.POST.get("username"))
    comments = Comment.objects.filter(comic_id=comic_id)
    template = render(request, 'comic.html', {
        'previous_url': reverse('comic', kwargs={'comic_id': comic_id - 1 if comic_id > 0 else len(images) - 1}),
        'next_url': reverse('comic', kwargs={'comic_id': comic_id + 1 if comic_id < len(images) - 1 else 0}),
        'comments': comments,
        'comic_url': images[comic_id]
    })
    return HttpResponse(template)


def comment(request):
    data = json.loads(request.body)
    comic_id = data.get('comic_id')
    text = data.get('text')
