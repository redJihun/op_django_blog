from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Blogapp
# Create your views here.


def home(request):
    blogapps = Blogapp.objects
    return render(request, 'home.html', {'blogapps': blogapps})

def detail(request, blogapp_id):
    blogapp_detail = get_object_or_404(Blogapp, pk=blogapp_id)
    return render(request, 'detail.html', {'blogapp': blogapp_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blogapp = Blogapp()
    blogapp.title = request.GET['title']
    blogapp.body = request.GET['body']
    blogapp.pub_date = timezone.datetime.now()
    blogapp.save()
    return redirect('/blogapp/' + str(blogapp.id))