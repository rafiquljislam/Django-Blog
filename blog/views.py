from django.shortcuts import render
from blog.models import Post

# Create your views here.

def bloghome(request):
    allpost = Post.objects.all()
    context = {
        'allpost':allpost
    }
    return render(request,'blog/bloghome.html',context)

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug)[0]
    context = {
        'post':post
    }
    return render(request,'blog/blogpost.html',context)