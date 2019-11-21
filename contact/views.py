from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.

from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        new = Contact.objects.create(name=name,
            email=email,
            message=message)
        new.save()

        messages.info(request,'Thank you, we will reach you soon..!')
        return redirect('contact')

    return render(request,'contact/contact.html')