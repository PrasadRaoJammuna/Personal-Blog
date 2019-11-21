from django.db import models
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django_resized import ResizedImageField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120,default='Unknown')

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural =("Categories")

    def __str__(self):
        return self.name



class Posts(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)   
    title = models.CharField(max_length=100,unique=True)
    description = RichTextUploadingField(blank=True, null=True)
   
    slug = models.SlugField()
    featured_image = ResizedImageField(size=[700, 400], upload_to='whatever', force_format='JPEG')
    
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField()
  

    class Meta:
        verbose_name = ("Posts")
        verbose_name_plural =("Posts")
        ordering =['-created_at']

    def __str__(self):
        return self.title




