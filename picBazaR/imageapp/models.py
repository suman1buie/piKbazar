from django.db import models
from django.contrib.auth.models import User


class Catagory(models.Model):
	des = models.TextField()
	title = models.CharField(max_length=20)
	def __str__(self):
		return self.title


class PostImage(models.Model):
	descriptions = models.CharField(max_length=200)
	catagory = models.ForeignKey(to=Catagory,on_delete = models.CASCADE)
	uploaded_by = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True, blank=True) 
	image = models.ImageField(upload_to='images//')
	cr_date = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
	user = models.OneToOneField(to = User,on_delete = models.CASCADE)
	first_name = models.CharField(max_length = 30,null=True,blank=True)
	last_name = models.CharField(max_length = 30,null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	profile_pic = models.ImageField(upload_to = 'profileImage//',null=True,blank=True)
	socal_link = models.CharField(max_length=100,null=True,blank=True)
	ph_no = models.CharField(max_length=10,null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
