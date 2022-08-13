from django.contrib import admin
from .models import Webqr, Imgqr

admin.site.register(Webqr)
admin.site.register(Imgqr)
# admin.site.register(FileQr)