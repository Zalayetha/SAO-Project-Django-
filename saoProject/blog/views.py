from unicodedata import category
from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
     post = Post.objects.all()
     categories = Post.objects.values('category').distinct()
   
     context ={
          'title' : 'Blog',
          'subTitle':'Welcome to Aincrad Blog Post',
          'Post' : post,
          'Category':categories,
     }

     return render(request,'blog/index.html',context)

def categoryPost(request,categoryInput):
     post = Post.objects.filter(category=categoryInput)
     categories = Post.objects.values('category').distinct()
   
     context ={
          'title' : 'Blog',
          'subTitle':'Welcome to Aincrad Blog Post',
          'Post' : post,
          'Category':categories,
     }

     return render(request,'blog/sub/categories.html',context)

def detailPost(request,slugInput):
     post = Post.objects.filter(slug=slugInput)
     categories = Post.objects.values('category').distinct()
   
     context ={
          'title' : 'Blog',
          'subTitle':'Welcome to Aincrad Blog Post',
          'Post' : post,
          'Category':categories,
     }

     return render(request,'blog/sub/detailPost.html',context)