from django.db import models
from django.contrib.auth.hashers import make_password, check_password

#Create your models here.


class userModel(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)


class sgModel(models.Model):
    uname = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    umail = models.EmailField(max_length=100)

    def set_password(self, raw_password):
        self.pwd = make_password(raw_password)
        
    def check_password(self,raw_password):
        return check_password(raw_password,self.pwd)

    def __str__(self):
        return self.uname

