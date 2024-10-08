"""ykcd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from lulz.views import random_lulz, comic, login_view, signup, logout_view, cv_view, typescript, freetrailer, freetrailer_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', random_lulz),
    path('comic/<int:comic_id>', comic, name='comic'),
    path('login/', login_view),
    path('signup/', signup),
    path('logout/', logout_view),
    path('CV/', cv_view),
    path('freetrailer/typescript/', typescript),
    path('freetrailer/', freetrailer),
    path('freetrailer/category/<str:category>', freetrailer_category, name='category')
]
