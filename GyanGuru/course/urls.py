#  create course related urls here .from django.urls import path
# from user_mgmt.views import LoginUserView, RegisterView, UserLogoutView
from os import path
from django.urls import path
from course.views import CoursePageView,CourseSingleView

app_name = "course"

urlpatterns = [
    path('coursepage/', CoursePageView.as_view(), name="coursepage"), 
    path('single/', CourseSingleView.as_view(), name="single"), 
]