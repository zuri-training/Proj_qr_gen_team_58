from distutils.command.upload import upload
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.




class Webqr(models.Model):
    name = models.CharField(max_length=1000)
    webqr_code = models.ImageField(upload_to='qr_codes', blank=True)


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


class Imgqr(models.Model):
    name = models.CharField(max_length=200)
    choice_img = models.ImageField(upload_to='choice_images')
    imgqr_code = models.ImageField(upload_to='qr_codes', blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        qr_image = Image.open(self.choice_img)
        qr_code = qrcode.make(qr_image)
        canvas = Image.new('RGB', (480,480), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_code)
        fname = f'qr_code-{self.created}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.imgqr_code.save(fname, File(buffer), save =True)
        canvas.close()
        super().save(*args, **kwargs)

        
