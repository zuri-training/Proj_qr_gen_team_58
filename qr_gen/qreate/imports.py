from cgitb import html
from multiprocessing import context
from unicodedata import name
from urllib import response
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import qreate
from .models import Webqr
from django.template.loader import get_template
# from xhtml2pdf import pisa
# from PIL import Image
# import qrcode
from io import BytesIO
# from django.core.files import File
# from PIL import Image, ImageDraw
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import UrlForm