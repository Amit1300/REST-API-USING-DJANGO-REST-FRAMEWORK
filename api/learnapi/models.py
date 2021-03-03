from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blogpost(models.Model):
    article=models.CharField(max_length=250)
    
    

class User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    
    
    


    