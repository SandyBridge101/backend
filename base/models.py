from django.db import models

# Create your models here.

class UserModel(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    password=models.CharField(max_length=200,null=True)
    is_rider = models.IntegerField(default=0)
    is_ready = models.IntegerField(default=0)
    ride=models.IntegerField(default=-1)
 
    def __str__(self):
        return self.phonenumber
    
class RideModel(models.Model):
    start = models.CharField(max_length=200,default='N/A')  
    destination = models.CharField(max_length=200,default='N/A')
    start_time=models.DateTimeField(null=True)
    end_time=models.DateTimeField(null=True)
    feedback = models.TextField(null=True)
    ratings = models.IntegerField(default=0)
    rider= models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    is_cancelled = models.IntegerField(default=0)
 
    def __str__(self):
        return self.start+' --> '+self.destination
    
