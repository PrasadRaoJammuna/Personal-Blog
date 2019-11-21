from django.forms import ModelForm 

from .models import Category,Posts



class PostForm(ModelForm):

    class Meta:
        model = Posts 
        fields =['author','category','title','description','slug','featured_image','published']

        

    