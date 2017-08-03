from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
# Create your views here.
class QRView(TemplateView):
    template_name = 'qrgenerator/qrcode.html'
