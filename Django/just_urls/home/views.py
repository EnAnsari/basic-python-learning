from django.shortcuts import render
from .forms import ContactUsForm
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def contactUs(request):
    sent = False
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            name = cd['name']
            email = cd['email']
            phone = cd['phone']
            message = cd['message']
            msg = f'name:{name}\nphone:{phone}\nemail:{email}\nmessage:\n{message}'
            from_email = 'en.ansari@outlook.com'
            to = 'rahmat2022a@gmail.com'
            sub = f'from contact of site: {subject}'
            sent = send_mail(sub, msg, from_email, [to], fail_silently=True)
            return render(request, 'home/forms/contact-us.html', {'form': form, 'sent': sent})
    form = ContactUsForm()
    return render(request, 'home/forms/contact-us.html', {'form': form, 'sent': sent})