from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    checked = models.BooleanField(default=False)



    class Meta:
        verbose_name = ("contact")
        verbose_name_plural = ("contacts")

    def __str__(self):
        return self.name

    
