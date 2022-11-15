from django.db import models

# Create your models here.

class regmodel(models.Model):
    fname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    phoneNumber=models.CharField(max_length=200,null=True)
    gen=models.CharField(max_length=200,null=True)
    adrs=models.CharField(max_length=200,null=True)
    District=models.CharField(max_length=200,null=True)

class orphanage_user(models.Model):
    name=models.CharField(max_length=200,null=True)
    aadhaar_no=models.CharField(max_length=200,null=True)
    age=models.CharField(max_length=200,null=True)
    gender=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    DOB=models.CharField(max_length=200,null=True)
    img=models.FileField(upload_to='proof_img')

class orphanagemodel(models.Model):
    orphanage_name=models.CharField(max_length=200,null=True)
    owner_name=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    contact_no=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=True)

class donationmodel(models.Model):
    username=models.CharField(max_length=200,null=True)
    Orphanagename=models.CharField(max_length=200,null=True)
    amount=models.CharField(max_length=200,null=True)
   
