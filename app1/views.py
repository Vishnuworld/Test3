from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def homepage(request):
    print("home page......! ")
    context = {}
    return render(request, "home.html", context=context)

def contact(request):
    """contact function based view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            sub = "Test Mail"
            body = {
            'first_name': form.cleaned_data['first_name'], 
            'last_name': form.cleaned_data['last_name'], 
            'email': form.cleaned_data['email_address'], 
            'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())
            try:
                send_mail(sub, message, 'admin@example.com', ['admin@example.com', 'abc@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Email sent succesfully." )
            return redirect ("homepage")
        messages.error(request, "Error. Message not sent.")
        return redirect ("homepage")
    form = ContactForm()
    return render(request, "contact.html", {'cont_form':form})


def func():
    return None

print("asd")
def func3():
    print("in func3")
    
def func1():
    print("in func1")
