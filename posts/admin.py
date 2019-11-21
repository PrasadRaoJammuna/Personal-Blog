from django.contrib import admin

# Register your models here.
from .models import Posts,Category



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    list_filter = ("published",'created_at')
    search_fields = ['title','author']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Posts,PostAdmin)
admin.site.register(Category)

