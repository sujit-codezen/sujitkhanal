from django.shortcuts import render, HttpResponse,redirect,get_object_or_404,reverse

from .models import Contact
from django.contrib import messages

# Create your views here.
def addContact(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if firstname=="" or lastname=='' or email=='' or message=='':
            messages.warning(request, "All fields Required")
            return redirect('/#contact')

        else:
            newContact = Contact(firstname=firstname, lastname=lastname, email=email, message=message)
            newContact.save()
            messages.success(request, "Message Sent Successfully.")
            return redirect('/#contact')