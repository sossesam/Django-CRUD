from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ' '
    success_url  = ' '


class PostUpdateView(UpdateView):
    model = Post
    fields = ' '
    success_url  = ' '

class PostDeleteView(DeleteView):
    model = Post
    fields = ' '
    success_url  = ' '