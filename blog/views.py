from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.http import HttpResponse
from requests.api import request
from .models import Post, Title
from .forms import PostForm
import requests
import json

def post_list(request):
    post_list = Post.objects.all().order_by('created_at')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {'posts':posts})


class post_detail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


@login_required
def post_create(request):
    form = PostForm()
    if(request.method == 'POST'):
        form = PostForm(request.POST)
        if(form.is_valid()):
            post_title = form.cleaned_data['title']
            post_body = form.cleaned_data['body']
            post_author = form.cleaned_data['author']
            post_status = form.cleaned_data['status']
            new_post = Post(title=post_title, body=post_body, author=post_author, status=post_status)
            new_post.save()
            return redirect('post_list')
    elif(request.method == 'GET'):
        return render(request, 'blog/add_post.html', {'form': form})

@login_required
def post_update(request, pk):
    data ={}
    post = Post.objects.get(pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    data['form'] = form
    data['post'] = post
    return render(request, 'blog/edit_post.html', data)

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')


def about(request):
    return render(request, 'blog/about_us.html')

def contact(request):
    return render(request, 'blog/contact.html')    





# testes
def get_titles():
    url = 'http://www.visualdicas.com.br/exemplos/json/cliente.json' 
    read = requests.get(url)
    titles = read.json()
    for title in titles:
        Title.objects.create(nome=title['nome'], cidade=title['cidade']) 