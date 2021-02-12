from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class TestPage(TemplateView):
    template_name = 'test.html'
