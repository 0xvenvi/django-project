from django.shortcuts import render
from .models import Backgroundimage

# Create your views here.


def home(request):
    img = Backgroundimage.objects.latest("id")
    return render(request, "../templates/home.html", context={"images": img})


def contacts(request):
    return render(request, "../templates/contacts.html", context={})
