from django.apps import AppConfig


class ImageappConfig(AppConfig):
    name = 'imageapp'
    def ready(self):
    	import imageapp.mysignal
