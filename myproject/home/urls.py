from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.handlesignup,name="signup"),
    path('login',views.handlelogin,name="login"),
    path('logout',views.handlelogout,name="logout"),
    path('student',views.student,name="student"),
   # path('students',views.students,name="students"),

]