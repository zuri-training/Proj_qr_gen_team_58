from django.shortcuts import render
from .models import Webqr
# Create your views here.
def home(request):
    return render(request, 'qreate/home.html', {})

def show_qr(request):
    name = "welcome to you qr code"

    obj = Webqr.objects.get(id=1)

    context = {
        'name': name,
        'obj': obj,
    }

    return render(request, 'qreate/show_qr.html', context)