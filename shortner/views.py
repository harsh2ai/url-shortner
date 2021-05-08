from django.shortcuts import render, redirect
import uuid

from django.http import HttpResponse
from .models import Url
# Create your views here.


def index(request, *args, **kwargs):
    return render(request, 'index.html')


def create(request, *args, **kwargs):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
