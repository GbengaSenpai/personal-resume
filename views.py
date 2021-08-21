from django.shortcuts import render, redirect
form .forms import ContactForm
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse

def home_view(request):
    return render(request, "index.htm/#about")

def contact(request):
    if request.method == 'POST':
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'name': form.cleaned_data['first_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'sorinolag@gmail.com', [sorinolag@gmail.com])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("main:homepage")

        form = ContactForm()
        return render(request, "index.htm", {'form':form})

