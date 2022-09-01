from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from course.models import Students
# Create your views here.
class CoursePageView(TemplateView):
    template_name = "main_pages/course-list-v1.html"
class CourseSingleView(TemplateView):
    template_name = "main_pages/course-single-v3.html"
class OrderCompleteView(TemplateView):
    template_name = "main_pages/shop-order-completed.html"
class EnrolledCourseView(TemplateView):
    template_name = "main_pages/enrolled-courses.html"
class LessonView(TemplateView):
    template_name = "main_pages/lesson-single-v1.html"
class InstructorSingleView(TemplateView):
    template_name = "main_pages/instructors-single.html"


# functions based views

def ADD(request):
     if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        emp = Students(
            name= name,
            email= email,
            student_data= password,
            
        )
        emp.save()
        return redirect('login')
     return render(request, 'index.html') 

