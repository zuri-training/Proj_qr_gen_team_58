from datetime import datetime
from distutils.command.upload import upload
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# import PyPDF2
import os
from django.conf import settings
from django.contrib.auth.models import User


class Webqr(models.Model):
    name = models.CharField(max_length=1000)
    webqr_code = models.ImageField(upload_to='qr_codes', blank=True)
    # created= models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.name)
        canvas = Image.new('RGB', (480,480), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_image)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.webqr_code.save(fname, File(buffer),  save=False)
        canvas.close()
        super().save(*args, **kwargs)
