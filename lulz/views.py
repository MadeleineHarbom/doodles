import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def random_lulz(request):
    images = ['IMG_0422.jpg', 'IMG_0427.jpg', 'IMG_0479.jpg', 'IMG_0480.jpg', 'IMG_0482.jpg']
    imgage = random.choice(images)
    template = render(request, "index.html", {'image_url': imgage})
    return HttpResponse(template)