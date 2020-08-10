from django.urls import path 
from django.views.generic import RedirectView
from . import views 


urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
    path('viewpost/<int:i_d>',views.viewpost),
    path('index/', views.Index),   
    path('upload/', views.PostCreate.as_view()),
    path('search/', views.search_something),
    path('page/<int:no>', views.homePage),
    path('deletePost/<int:i_d>', views.DeletePost),
    path('editPost/<int:pk>', views.EditPostView.as_view(success_url='/imageapp/home/')),
    path('registers/', views.sign_up),
    path('signin/', views.sign_in),
    path('logout/', views.log_out),
    path('singleview/<int:i_d>', views.particuler_view),
    path('editprofile/<int:pk>',views.ProfileUpdateView.as_view(success_url='/imageapp/home/')),
    path('viewprofile/<int:i_d>',views.view_profile),
    path('catagory/<int:i_d>', views.catagory_view),
    path("",RedirectView.as_view(url = 'index/'))
]
