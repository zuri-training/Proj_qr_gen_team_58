from django.shortcuts import render
# from django.http import HttpResponseRedirect
from .models import Webqr
from .forms import UrlForm
# Create your views here.

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



def show_qr(request):
    qr_list = Webqr.objects.all()

    return render(request, 'qreate/show_qr.html', {'qr_list':qr_list})


def home(request):
    return render(request, 'qreate/home.html', {})

