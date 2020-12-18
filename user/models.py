from django.db import models

# Create your models here.


class login(models.Model):
    username=models.CharField(max_length=120)
    password=models.CharField(max_length=120)


    def __str__(self):
        return self.username

class Profile(models.Model):
    user=models.CharField(max_length=120)
    date_of_birth=models.DateField(blank= True,null=True)
    sex = models.CharField(max_length=15, default='')
    qualification=models.TextField(max_length=500)
    job_experience=models.TextField(max_length=500)
    upload_resume=models.FileField(upload_to="documents/")
    profile_pic=models.ImageField(upload_to="images",default='')


    def __str__(self):
        return self.user

class employerProfile(models.Model):
    user=models.CharField(max_length=120,default='')
    company_name=models.CharField(max_length=120)
    job_details=models.TextField(max_length=350)
    phonenumber=models.CharField(max_length=120)
    email_id=models.EmailField()


    def __str__(self):
        return self.company_name

class addJob(models.Model):
    user = models.CharField(max_length=120,default='')
    company_name = models.CharField(max_length=120)
    job_title= models.CharField(max_length=120,default='')
    skills= models.CharField(max_length=120,default='')
    experience= models.CharField(max_length=120,default='')
    job_details = models.TextField(max_length=250)
    phonenumber = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=50)


    def __str__(self):
        return self.company_name

