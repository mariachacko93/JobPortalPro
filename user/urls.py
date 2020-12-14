"""JobPortalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import register,login_view,logout_view,profile_create,home,view_profile,edit_profile,employerLogin,employerRegister
from user.views import add_job,view_jobs,apply,search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/",register,name="register"),
    path("login/",login_view,name="login"),
    path("logout/",logout_view,name="logout"),
    path("createprofile/",profile_create,name="create"),
    path("home/",home,name="home"),
    path("viewprofile/",view_profile,name="viewprofile"),
    path("editprofile/",edit_profile,name="editprofile"),
    path("employerregister/",employerRegister,name="employerreg"),
    path("employerlogin/",employerLogin,name="employerlogin"),
    path("addjob/",add_job,name="addjob"),
    path("applyjobs/",view_jobs,name="applyjobs"),
    path("apply",apply,name="apply"),
    path("searchjobs/",search,name="search"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
