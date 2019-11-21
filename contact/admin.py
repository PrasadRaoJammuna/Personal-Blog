from django.contrib import admin
from .models import Contact

# Register your models here.
class contactAdmin(admin.ModelAdmin):
     date_hierarchy ='created'
     list_display = ['name','email','message','created','checked']
     list_filter =['created','checked']
     list_editable =['checked']






admin.site.register(Contact,contactAdmin)

#admin.site.register(Contact)


