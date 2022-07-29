from django.shortcuts import render, HttpResponse
from .models import Webqr
# Create your views here.
def home(request):
    return render(request, 'qreate/home.html', {})


#function generated qr for website link
def generate_web_qr(request):
    if request.method =="POST":
        try:
            # String which represents the QR code
            qrname= request.POST['name']
            text= request.POST['url']
            foo= Webqr.objects.get_or_create(name=qrname)
            foo= Webqr.objects.get(name=qrname)
            foo.data= text
            foo.save()
            test= Webqr.objects.get(name=qrname)
            return render(request, 'qreate/show_qr.html',{'test':test})
        except Exception as err:
            return HttpResponse('<p>an error occured</p>')

    else:
        return render(request,'qreate/show_qr.html')   

#function generates url for email mesage
def email_qr(request):
    if request.method == "POST":
        try:
            # String which represents the QR code
            qrname= request.POST['name']
            text = f"mailto:{request.POST['to']}?subject={request.POST['subject']}&body={request.POST['body']}"
            get_qr= Webqr.objects.get_or_create(name= qrname)
            get_qr= Webqr.objects.get(name= qrname)
            get_qr.data=text
            get_qr.save()
            new_qr= Webqr.objects.get(name=qrname)
            return render(request, 'qreate/show_email_qr.html',{'test':new_qr})
        except Exception as err:
            return HttpResponse('<p>an error occured</p>')
    else:
        return render(request, 'qreate/show_email_qr.html')