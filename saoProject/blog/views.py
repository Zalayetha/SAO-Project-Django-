from django.shortcuts import render,redirect
from .models import Post
from .forms import CreatePost
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
     data = CreatePost(request.POST or None)
     if request.method == 'POST':
          if data.is_valid():
               data.save()
               # print("{},{}".format(data.cleaned_data,request.POST))
               return redirect('blog:index')
            
     context ={
          'title' : 'Blog',
          'subTitle':'Create Post',
          'Data' : data,
     }
          

     return render(request,'blog/sub/createPost.html',context)