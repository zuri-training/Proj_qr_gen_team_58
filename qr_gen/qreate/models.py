from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.

class Webqr(models.Model):
    name = models.CharField(max_length=200)
    data = models.CharField(max_length=1000, blank=True)
    webqr_code = models.ImageField(upload_to='qr_codes', blank=True)


    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.data)
        canvas = Image.new('RGB', (480,480), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_image)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.webqr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)