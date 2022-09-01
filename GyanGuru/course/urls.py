#  create course related urls here .from django.urls import path
# from user_mgmt.views import LoginUserView, RegisterView, UserLogoutView
from os import path
from django.urls import path
from course import views
from course.views import CoursePageView,CourseSingleView,OrderCompleteView,EnrolledCourseView,LessonView,InstructorSingleView


app_name = "course"

urlpatterns = [
    path('coursepage/', CoursePageView.as_view(), name="coursepage"), 
    path('single/', CourseSingleView.as_view(), name="single"), 
    path('order/', OrderCompleteView.as_view(), name="order"), 
    path('enrolled/', EnrolledCourseView.as_view(), name="enrolled"), 
    path('lesson/', LessonView.as_view(), name="lesson"), 
    path('instructor/', InstructorSingleView.as_view(), name="instructor"), 
    path('add/', views.ADD, name="add"), 
]