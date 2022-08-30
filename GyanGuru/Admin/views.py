from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
# Create your views here.
class HomePageView(TemplateView):
    
    template_name = "main_pages/index.html"
class LoginPageView(TemplateView):
    
    template_name = "main_pages/login.html"