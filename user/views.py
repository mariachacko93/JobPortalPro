from django.shortcuts import render,redirect
from user.forms import registrationForm,loginForm,createProfileForm,employerRegisterForm
from django.contrib.auth import authenticate,login,logout
from user.forms import addJobForm,searchForm
from user.models import Profile,addJob
from django.core.paginator import Paginator
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
            return render(request,"users/userhome.html")

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
from django.db.models.fields import DateField

def view_jobs(request):
   job=addJob.objects.all().order_by("dateposted")[::-1]
   context = {}
   context["job"] = job

   return render(request, "users/applyjobs.html",context)

def apply(request):
    return render(request, "users/sucesspage.html")



def searchpage(request):
    return render(request, "users/serjob.html")



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q


def job_search(request):
        if request.method == 'GET':
            query = request.GET.get('q')

            submitbutton = request.GET.get('submit')
            if query is not None:
                results =addJob.objects.filter(Q(company_name__icontains=query) | Q(experience__icontains=query) | Q(job_title__icontains=query) | Q(locatns__icontains=query) | Q(skills__icontains=query)).distinct().order_by("dateposted")[::-1]

                # paginator start

                  # 2 posts per page
                paginator = Paginator(results,4)
                # page = request.GET.get('page')
                try:
                    page = int(request.GET.get('page', '1'))
                except:
                    page = 1
                try:
                    results = paginator.page(page)
                except PageNotAnInteger:
                    results = paginator.page(1)
                except EmptyPage:
                    results = paginator.page(paginator.num_pages)

                context = {
                        'page':page,
                        'results': results,
                        'submitbutton': submitbutton,
                               }

                return render(request, "users/serjob.html", context)

                # pagiinator ends
            else:
                return render(request, 'users/serjob.html')