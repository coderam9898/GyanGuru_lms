from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView, CreateView, UpdateView
# Create your views here.
class CoursePageView(TemplateView):
    template_name = "main_pages/course-list-v1.html"
class CourseSingleView(TemplateView):
    template_name = "main_pages/course-single-v3.html"
class OrderCompleteView(TemplateView):
    template_name = "main_pages/shop-order-completed.html"
class EnrolledCourseView(TemplateView):
    template_name = "main_pages/enrolled-courses.html"
