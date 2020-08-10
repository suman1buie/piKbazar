from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import Catagory , UserProfile , PostImage
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import  User,auth
from django.views.generic import DetailView
from django.views.generic import ListView
from . forms import SignUpForm 
from django.views.generic.edit import CreateView , UpdateView
from django.contrib.messages.views import SuccessMessageMixin
# from django.views.generic import templateView


def viewpost(request,i_d):
	posts = PostImage.objects.get(pk=i_d)
	return render(request,'viewPost.html',{'posts':posts})


def sign_up(request):
	if request.method == 'POST':
		form      = SignUpForm(request.POST)
		email     = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1!=password2:
			messages.error(request,"password no match!!! Try again")
			return redirect('/imageapp/registers/')

		elif User.objects.filter(email=email).exists():
			messages.error(request,"Email Allredy Register.. !!Try new One..!")
			return redirect('/imageapp/registers/')

		elif form.is_valid():
			form.save()
			messages.success(request,"Account create successfully! :)\n Now Log In")
			return redirect('/imageapp/signin/')
		else:
			messages.error(request,'Unsuccessful :(.... try again!!!')
			return redirect('/imageapp/registers/')
	else:
		form = SignUpForm()
	return render(request,"singup.html",{'form':form})


def sign_in(request):
	message_class=""
	er_message=""
	flag = False
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			messages.success(request,"You loged In successfully!!!")
			return redirect('/imageapp/home/')
		else:
			messages.error(request,"invalid username or password")
			return redirect('/imageapp/signin/')
	else:
		return render(request,"signin.html",{})

def log_out(request):
	auth.logout(request)
	messages.success(request,"You Loged Out Successfully !")
	return redirect('/imageapp/home/')

def homePage(request,no):
	start      = (no-1)*9;
	end        = int(no)*9
	cat        = Catagory.objects.all()
	image      = PostImage.objects.all()
	pag       = no
	t_page = float(len(image))/9
	# print(t_page)
	if t_page >float(int(t_page)):
		t_page = int(t_page)+1
	total_page = []
	t_page  = t_page+1;
	for i in range(1,t_page):
		total_page.append(i)

	if len(image)<end:
		end = len(image)
	imagess    = image[start:end]

	# print(len(total_page))
	data = {'imagess':imagess,'cat':cat, 'pag':pag,'total_page':total_page}
	return render(request,'home.html',data)


def home(request):
	cat     = Catagory.objects.all()
	image   = PostImage.objects.all()
	# for im in image:
		# print(im.id)
	# print(len(imagess))
	t_page = float(len(image))/9
	imagess    = image[:9]
	# print(t_page)
	if t_page >float(int(t_page)):
		t_page = (t_page)+1
	total_page = []
	t_page = int(t_page)
	t_page = t_page + 1
	for i in range(1,t_page):
		total_page.append(i)

	pag = 1
	# print(len(total_page))
	data = {'imagess':imagess,'cat':cat,'total_page':total_page,'pag':pag}
	return render(request,'home.html',data)


def catagory_view(request,i_d):
	cat = Catagory.objects.all()
	cats  = Catagory.objects.get(pk = i_d)
	imagess = PostImage.objects.filter(catagory = cats)
	t_image = len(imagess)
	total_page = []
	data = {'imagess':imagess,'cat':cat}
	return render(request,'home.html',data)

# def catagort_page(request,page):
# 	cat  = Catagory.objects.all()
# 	cats = Catagory.objects 


def search_something(request):
	item = request.POST.get("dowork")
	if item is not None:
		imagess = PostImage.objects.filter(Q(descriptions__startswith=item))
	else:
		imagess = PostImage.objects.all()
	cat = Catagory.objects.all()
	l = True
	if len(imagess)>0:
		l = False
	data = {'imagess':imagess,'cat':cat,'l':l}
	return render(request,'home.html',data)


@method_decorator(login_required, name="dispatch")
class PostCreate(CreateView):
	template_name = "uploadFile.html"
	model  = PostImage
	fields = ["descriptions","catagory","image"]
	def form_valid(self,form):
		self.objects = form.save()
		self.objects.uploaded_by = self.request.user
		self.objects.save()
		messages.success(self.request,"Your Post Upload successfully!")
		return redirect('/imageapp/home/')



def view_profile(request,i_d):
	profile = User.objects.get(pk=i_d)
	alldetail = UserProfile.objects.get(user=profile.id)
	print(alldetail.id)
	flag = str(alldetail.profile_pic).startswith('profileImage/')
	f1=False
	if alldetail.socal_link is not None:
		f1 = True;
	return render(request,'viewprofile.html',{'alldetail':alldetail,'flag':flag,'f1':f1})


@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(SuccessMessageMixin,UpdateView):
	template_name = 'editprofile.html'
	model  		  = UserProfile
	fields 		  = ['first_name','last_name','profile_pic','socal_link','ph_no','description'] 
	success_url = '/imageapp/home/'
	success_message = "profile updae successfully"


@method_decorator(login_required, name="dispatch")
class EditPostView(SuccessMessageMixin,UpdateView):
	template_name   = 'editPost.html'
	model  	        = PostImage
	fields          = ['descriptions','catagory','image']
	success_url     = '/imageapp/home/'
	success_message =  "Post Update Successfully! :)"

@login_required
def particuler_view(request,i_d):
	print(i_d)
	item    = User.objects.get(pk=i_d)
	imagess = PostImage.objects.filter(uploaded_by=item)
	cat = Catagory.objects.all()
	return render(request,"home.html",{'imagess':imagess,'cat':cat})

@login_required
def DeletePost(request,i_d):
	message_class="alert-success"
	er_message="Your Post Delete Successfully"
	want_to_delete_item = PostImage.objects.get(id=i_d)
	want_to_delete_item.delete()
	messages.success(request,"Post Delete Successfully :)")
	return redirect('/imageapp/home/')

def Index(request):
	return render(request,"index.html",{})

def  admin_view(request):
	if request.user.is_authenticated:
		if request.user.is_superuser:
			return redirect('/adminreal/')
		else:
			return redirect('/imageapp/home/')
	else:
		return redirect('/imageapp/home/')


def about(request):
	return render(request,'about.html',{})