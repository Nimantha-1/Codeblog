from django.shortcuts import render, HttpResponse
from . models import Post

def bloghome(request):
    allpost = Post.objects.all()
    context = {
        'allpost':allpost
    }
    return render(request, "blog/bloghome.html", context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {
        'post':post
    }
    return render(request, "blog/blogpost.html", context)