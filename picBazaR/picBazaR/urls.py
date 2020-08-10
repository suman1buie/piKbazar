from django.contrib import admin
from django.urls import path , include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from imageapp import views

urlpatterns = [
    path('admin/', views.admin_view),
    path('adminreal/', admin.site.urls),
    path('imageapp/', include('imageapp.urls')),
    path("",RedirectView.as_view(url = 'imageapp/'))
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
