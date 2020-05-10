from django.shortcuts import render,redirect
from .forms import ContactForm

from django.core.mail import  BadHeaderError
from django.core.mail import  send_mail  as sm
from django.http import HttpResponse , HttpResponseRedirect

# Create your views here.

from .models import ContactDetails

def  send_mail(request):
    contactdetails = ContactDetails.objects.last()

    if  request.method =='POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']

            try:
                sm(subject,message,from_email,['test@gmail.com'])

            except BadHeaderError:
                return HttpResponse('invalid header ')

            return redirect('contact:success')


    else:
         contact_form = ContactForm()


    template = 'contact/contact.html'

    context = {
                'contactdetails' : contactdetails ,
                'contact_form' : contact_form 
    }

    return render(request, template, context)

def success(request):
    return HttpResponse('Message Sent Successfully ')
