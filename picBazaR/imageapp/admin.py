from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . models import *


class PostAdmin(ModelAdmin):
	list_display  = ['uploaded_by','cr_date']
	search_fields = ['uploaded_by' , 'catagory']
	list_filter   = ['cr_date']

class UserAdmin(ModelAdmin):
	list_display  = ['user']
	search_fields = ['user']
	list_filter   = ['user']

admin.site.register(Catagory)
admin.site.register(UserProfile,UserAdmin)
admin.site.register(PostImage,PostAdmin)
