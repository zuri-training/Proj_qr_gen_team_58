from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def support(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
        
            subject = "Website Inquiry"
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, "info@qreate.com", ["info@qreate.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")

            # TODO: Redirect to homepage
            return HttpResponse("Thanks for contacting")
        return HttpResponse(f'{form.errors}')
    else:
        form = ContactForm()

    return render(request, "common/support.html", {"contact_form": form})
