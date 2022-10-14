from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

# Create your views here.
# CBV


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

# FBV
# def home(request):
#     posts = Post.objects.all()
#     context = {'posts': posts}

#     return render(request, 'home.html', context)
