from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Posts,Category

from .forms import PostForm



def blog(request):
    posts = Posts.objects.all().order_by('-published')
    cats = Category.objects.all()

    return render(request,'posts/blog.html',{'posts':posts,'cats':cats})


def post(request,slug):
    posts = Posts.objects.filter(slug=slug)
    cats = Category.objects.all()
    
    return render(request,'posts/post.html',{'posts':posts,'cats':cats})


def category(request,name):   
    cats = Category.objects.all() 
    posts =  Posts.objects.filter(category__name=name)
   
    return render(request,'posts/blog.html',{'posts':posts,'cat':name,'cats':cats})


def categories(request):
    cats = Category.objects.all()
    
    return render(request,'widget.html',{'cats':cats})

@login_required
def dashboard(request):
    posts = Posts.objects.all()
    return render(request,'posts/dashboard.html',{'posts':posts})



@login_required
def add_new(request):
    form = PostForm()
    if request == 'POST':
        form = PostForm(request.POST or None,request.FILES or None)
        if form.is_valid():
           form.save() 
           form = PostForm()


    return render(request,'posts/new_post.html',{'form':form})



@login_required
def delete(request,id):
    item = get_object_or_404(Posts,id=id)
    item.delete()
    return redirect('dashboard')



@login_required
def edit(request,id):
    item = get_object_or_404(Posts,id=id)
    form = PostForm(request.POST or None,request.FILES or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('dashboard')
    
    return render(request,'posts/new_post.html',{'form':form})


