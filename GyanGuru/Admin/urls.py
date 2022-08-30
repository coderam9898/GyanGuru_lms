from django.urls import path
# from user_mgmt.views import LoginUserView, RegisterView, UserLogoutView
from Admin.views import HomePageView

app_name = "Admin"

urlpatterns = [
    path('index/', HomePageView.as_view(), name="index"),
   
    
]