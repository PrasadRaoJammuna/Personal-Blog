from django.shortcuts import render
from posts.models import Posts,Category
from django.db.models import Q
from .models import Search
from django.db.models import F



# Create your views here.
def search(request):
    
    query = request.GET.get('q',None)
    posts = Posts.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query) | Q(description__icontains=query) )
    
    if Search.objects.filter(query=query).exists():
        Search.objects.filter(query=query).update(search_count =F('search_count')+1)
             
    else:
        Search.objects.create(query=query)
    
    cats = Category.objects.all()

    return render(request,'search/search.html',{'query':query,'posts':posts,'cats':cats})

