from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),    
    path('register', views.register, name='register'),
    path('getruth', views.getruth, name='getruth'),
    path('getdare', views.getdare, name='getdare')
]