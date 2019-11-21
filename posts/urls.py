from django.urls import path 


from .views import blog,post,category,dashboard,delete,add_new,edit

urlpatterns = [
    path('',blog,name='blog'),
    path('post/<str:slug>/',post,name='posts'),
    path('category/<str:name>/',category,name='category'),
    path('dashboard/',dashboard,name='dashboard'),
    path('delete/<int:id>/',delete,name='delete'),
    path('edit/<int:id>/',edit,name='edit'),
    path('add_new/',add_new,name='add_new'),
    
]
