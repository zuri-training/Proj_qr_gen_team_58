from cgitb import html
from multiprocessing import context
from urllib import response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import qreate
from .models import Webqr
from .forms import UrlForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from PIL import Image


# from django.conf import settings
# from django.template.loader import render_to_string
# import weasyprint


# def qr_pdf(request, *args, **kwargs):
#     object_pk = kwargs.get('pk')
#     mypdf = get_object_or_404(Webqr, pk=object_pk)
#     html = render_to_string('qreate/pdf.html', {'mypdf': mypdf})
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'filename=pdf_{mypdf.pk}.pdf'
#     weasyprint.HTML(string=html).write_pdf(response)

#     return response



def qr_jpg(request, *args, **kwargs):
    object_pk = kwargs.get('pk')
    my_object = get_object_or_404(Webqr, pk=object_pk)
    my_img = my_object.webqr_code
    context = {
        'my_img': my_img
    }
    return render(request, 'qreate/download_jpg.html', context)


# code to convert qrcode to pdf
def qr_pdf(request, *args, **kwargs):
    object_pk = kwargs.get('pk')
    mypdf = get_object_or_404(Webqr, pk=object_pk)
    # mypdf= Webqr.objects.get(pk=26)
    template_path = 'qreate/pdf.html'
    context = {'mypdf': mypdf}

    response = HttpResponse(content_type ='application/pdf')
    # # if download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
   
    response['Content-Disposition'] = 'filename=qrcode.pdf'
    # # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
     

# code to render the newly added qr code
def created_qr(request):
    qr_list = Webqr.objects.last()
    return render(request, 'qreate/created_qr.html', {'qr_list':qr_list})


# code to add a new qr code
def add_qr(request):
    submitted = False
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
            qr_list = Webqr.objects.last()
            return render(request, 'qreate/created_qr.html', {'qr_list':qr_list})
            
    else:
        form = UrlForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'qreate/add_qr.html', {'form':form, 'submitted':submitted })


# code to show all the qr codes in the database.
def show_qr(request):
    qr_list = Webqr.objects.all()

    return render(request, 'qreate/show_qr.html', {'qr_list':qr_list})


def home(request):
    return render(request, 'qreate/home.html', {})


#function generates url for email mesage
# def email_qr(request):
#     if request.method == "POST":
#         try:
            # String which represents the QR code
        #     qrname= request.POST['name']
        #     text = f"mailto:{request.POST['to']}?subject={request.POST['subject']}&body={request.POST['body']}"
        #     get_qr= Webqr.objects.get_or_create(name= qrname)
        #     get_qr= Webqr.objects.get(name= qrname)
        #     get_qr.data=text
        #     get_qr.save()
        #     new_qr= Webqr.objects.get(name=qrname)
        #     return render(request, 'qreate/show_email_qr.html',{'test':new_qr})
        # except Exception as err:
        #     return HttpResponse('<p>an error occured</p>')
    # else:
    #     return render(request, 'qreate/show_email_qr.html')
