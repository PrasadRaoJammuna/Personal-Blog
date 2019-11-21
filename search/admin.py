from django.contrib import admin

# Register your models here.

from .models import Search



class SearchAdmin(admin.ModelAdmin):
    date_hierarchy ='timestamp'
    list_display = ['query','search_count','timestamp']
    list_filter =['search_count','timestamp']



admin.site.register(Search,SearchAdmin)






