from django.shortcuts import render,redirect
from user.forms import registrationForm,loginForm,createProfileForm,employerRegisterForm
from django.contrib.auth import authenticate,login,logout
from user.forms import addJobForm
from user.models import Profile,addJob

# Create your views here.



def register(request):
    form=registrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=registrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context["form"]=form
            return render(request, "users/register.html", context)

    return render(request,"users/register.html",context)


def login_view(request):

    if request.method=="POST":

            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
            return render(request,"users/home.html")

    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def home(request):
    return render(request,"users/userhome.html")

def profile_create(request):
    form=createProfileForm(initial={"user":request.user})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=createProfileForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("viewprofile")
        else:
            context["form"]=form
            return render(request, "users/createprofile.html", context)

    return render(request,"users/createprofile.html",context)

# def edit_profile(request):
#     user = Profile.objects.get(user=request.user)
#     form=createProfileForm()
#     context={}
#     context["form"]=form
# #     if request.method=="POST":
# #         form=createProfileForm(data=request.POST,files=request.FILES)
# #         if form.is_valid():
#             form.save()
#             return redirect("viewprofile")
#         else:
#             context["form"]=form
#             return render(request, "users/editprofile.html", context)
#
    # return render(request,"users/editprofile.html",context)

def edit_profile(request):
    user = Profile.objects.get(user=request.user)
    form=createProfileForm(initial={"user":request.user},instance=user)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=createProfileForm(instance=request.user,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("inside")
            return redirect("home")
        else:
            context["form"]=form
            return render(request, "users/editprofile.html", context)

    return render(request,"users/editprofile.html",context)



def view_profile(request):
    user=Profile.objects.get(user=request.user)
    context={}
    context["user"]=user
    return render(request,"users/viewprofile.html",context)

# Employer codes-->

def employerRegister(request):
    form=employerRegisterForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=employerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context["form"]=form
            return render(request, "users/register.html", context)

    return render(request,"users/register.html",context)

def employerLogin(request):
    form=loginForm()
    context={}
    context["form"]=form

    if request.method=="POST":
        form=loginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
            return render(request,"users/home.html",context)
    else:
        context["form"]=form
        return render(request, "users/home.html", context)
    return render(request,"users/home.html",context)

# def logout_employer(request):
#     logout(request)
#     return redirect("login")


def add_job(request):
    form=addJobForm()
    context={}
    context["form"]=form
    if request.method == "POST":
        form = addJobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("applyjobs")
        else:
            context["form"] = form
            return render(request, "users/addjob.html", context)

    return render(request,"users/addjob.html",context)

def view_jobs(request):
   job=addJob.objects.filter(user=request.user)
   context = {}
   context["job"] = job
   return render(request, "users/applyjobs.html", context)

def apply(request):
    return render(request, "users/sucesspage.html")

def search(request):
    search=addJob.objects.filter(job_title__icontains="developer")
    context={}
    context["search"]=search
    return render(request, "users/searchjobs.html")


# def search_view(request):
#     jobs = addJob.objects.all()
#     form = addJobForm(request.GET)
#     if form.is_valid():
#         if form.cleaned_data["job_title"]:
#             jobs = addJob.filter(name__icontains=form.cleaned_data["job_title"])
#         elif form.cleaned_data["company_name"]:
#             jobs = addJob.filter(company_name=form.cleaned_data["company_name"])
#
#     return render(request, "users/searchjobs.html",
#             {"form": form, "search_list": jobs})
