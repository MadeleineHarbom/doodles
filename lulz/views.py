import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg']


def random_lulz(request):
    imgage = random.choice(images)
    template = render(request, "index.html", {'image_url': imgage})
    return HttpResponse(template)


def comic(request, comic_id):
    template = render(request, 'comic.html', {
        'previous_url': reverse('comic', kwargs={'comic_id': comic_id - 1 if comic_id > 0 else len(images) - 1}),
        'next_url': reverse('comic', kwargs={'comic_id': comic_id + 1 if comic_id < len(images) - 1 else 0}),
        'comic_url': images[comic_id]
    })
    return HttpResponse(template)
