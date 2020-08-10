from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from . models import UserProfile


@receiver(post_save,sender=User)
def save_post(sender, instance, created, **kwarg):
	if created:
		UserProfile.objects.create(user = instance ,  first_name = instance.first_name , email = instance.email, last_name = instance.last_name )