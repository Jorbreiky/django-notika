from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..formularios.post import PostForm
from ..modelos.post import Post

class Post():
    
    def index(self, request):
        posts = Post.objects.all();
        context = {'posts': posts}
        return render(request, 'post_all.html', context)
    
    def add(self, request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('/post/')
        else:
            form = PostForm()
            context = { 'form': form}
            return render(request, 'post_add.html', context)