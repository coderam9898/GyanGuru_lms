from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView, CreateView, UpdateView
# Create your views here.
class CoursePageView(TemplateView):
    template_name = "main_pages/course-list-v2.html"
class CourseSingleView(TemplateView):
    template_name = "main_pages/course-single-v5.html"
