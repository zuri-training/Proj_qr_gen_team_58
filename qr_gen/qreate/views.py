
from django.shortcuts import render, HttpResponse
# from django.http import HttpResponseRedirect
from .models import Webqr
from .forms import UrlForm
# Create your views here.

def home(request):
    return render(request, 'qreate/home.html')

def created_qr(request):
    qr_list = Webqr.objects.last()
    return render(request, 'qreate/created_qr.html', {'qr_list':qr_list})

def add_qr(request):
    submitted = False
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
            qr_list = Webqr.objects.last()
            return render(request, 'qreate/created_qr.html', {'qr_list':qr_list})
            # return render(request, 'qreate/created_qr.html')
    else:
        form = UrlForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'qreate/add_qr.html', {'form':form, 'submitted':submitted })



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
