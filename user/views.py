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

def view_jobs(request):
   job=addJob.objects.all()
   context = {}
   context["job"] = job
   print(job)
   return render(request, "users/applyjobs.html",context)

def apply(request):
    return render(request, "users/sucesspage.html")



def searchpage(request):
    return render(request, "users/serjob.html")

# def search(request):
#     form=searchForm()
#     context={}
#     context["form"]=form
#
#     if request.method=="POST":
#         form=loginForm(request.POST)
#         if form.is_valid():
#               jobsearch=addJob.objects.all()
#               context["jobsearch"]=jobsearch
#     #         company_name=form.cleaned_data.get("company_name")
#     #         job_title=form.cleaned_data.get("job_title")
#     #         skills=form.cleaned_data.get("skills")
#     #         experience=form.cleaned_data.get("experience")
#     #         searchjob=authenticate(request,company_name=company_name,job_title=job_title,skills=skills,experience=experience)
#     #         if searchjob:
#     #             # sear=addJob.objects.filter(company_name="company_name")
#     #             # print(sear)
#     #             print(company_name,job_title,skills)
#               return redirect("search")
#         else:
#                 context["form"]=form
#                 return render(request, "users/home.html", context)
#
#     return render(request,"users/serjob.html",context)


# def job_search(request):
#     query = request.GET.get('p')
#     object_list = []
#     if(query == None):
#         jobs = addJob.objects.all()
#         context={}
#         context["jobs"]=jobs
#     else:
#
#         company_name = addJob.objects.filter(
#             company_name__icontains=query).order_by()
#         job_title = addJob.objects.filter(
#             job_title__icontains=query).order_by()
#         skills= addJob.objects.filter(
#             skills__icontains=query).order_by()
#         # job_type_list = addJob.objects.filter(
#         #     job_type__icontains=query).order_by('-date_posted')
#         for i in company_name:
#             object_list.append(i)
#         for i in job_title:
#             if i not in object_list:
#                 object_list.append(i)
#         for i in skills:
#             if i not in object_list:
#                 object_list.append(i)
#         # for i in job_type_list:
#         #     if i not in object_list:
#         #         object_list.append(i)
#     # if(loc == None):
#     #     locat = addJob.objects.all()
#     # # else:
#         # locat = addJob.objects.filter(
#         #     location__icontains=loc).order_by('-date_posted')
#     final_list = []
#     # for i in object_list:
#     #     if i in locat:
#     #         final_list.append(i)
#     paginator = Paginator(final_list, 20)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'addJob': page_obj,
#         'query': query,
#     }
#     return render(request,"users/serjob.html", context)

# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# from django.views.generic import ListView
# from django.http import HttpResponse
def job_search(request):
        if request.method == 'GET':
            query = request.GET.get('q')

            submitbutton = request.GET.get('submit')

            if query is not None:
                lookups = Q(company_name__icontains=query) | Q(experience__icontains=query) | Q(job_title=query)

                results = addJob.objects.filter(lookups).distinct()

                context = {'results': results,
                           'submitbutton': submitbutton}

                return render(request, 'users/serjob.html', context)

            else:
                return render(request, 'users/serjob.html')