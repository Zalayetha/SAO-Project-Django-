from django.shortcuts import render
from .models import Post
from .forms import CreatePost
from django.http import HttpResponseRedirect 
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

def create(request):
     data = CreatePost()
     if request.method == 'POST':
          Post.objects.create(
               subject = request.POST.get('subject'), 
               category = request.POST.get('category'),
               body = request.POST.get('body'),
          )
          return HttpResponseRedirect("/blog/")

     context ={
          'title' : 'Blog',
          'subTitle':'Create Post',
          'Data' : data,
     }
          

     return render(request,'blog/sub/createPost.html',context)