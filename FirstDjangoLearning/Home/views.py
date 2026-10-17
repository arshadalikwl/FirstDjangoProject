from datetime import datetime

from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.http import require_http_methods
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages

from Home.models import Contact

# Create your views here.
def index(request):
    content ={
        'price' : 1100
    }
    return render(request,"index.html",content)   

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name').strip()
        email= request.POST.get('email').strip()
        subject= request.POST.get('subject').strip()
        message= request.POST.get('message').strip()
        if not all([name, email, subject, message]):
            messages.error(request, "please fill all the fields")
            return redirect('contact')
        if len(name) > 100 or len(email) > 254:
            messages.error(request, "Name or email is too long")
            return redirect('contact')
        if len(subject) > 200 or len(message) > 2000:
            messages.error(request, "Subject or message is too long")
            return redirect('contact')
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email address")
            return redirect('contact')
        
        #validation completed
        contact = Contact(name=name, email=email, subject=subject, message=message,date=datetime.today())
        contact.save()
        messages.success(
            request, "Your message has been sent successfully. We will get back to you soon."
        )
        return redirect('contact')

    return render(request,"contact.html")
