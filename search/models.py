from django.db import models

# Create your models here.

class Search(models.Model):
    query = models.CharField(max_length=100)
    search_count = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Search'
        verbose_name_plural = 'searches'

    def __str__(self):
        return self.query


        
