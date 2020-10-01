from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('website.html', views.index),
    path('news.html', views.news),
    path('involved.html', views.involved),
    path('mission.html', views.mission),
    path('news2.html', views.news2),
    path('news2.0.html', views.news2_0),
    path('news3.html', views.news2),
    path('news4.html', views.news4),
    path('news5.html', views.news5),
    path('news6.html', views.news6),
    path('news7.html', views.news7),
    path('news8.html', views.news8),
    path('news9.html', views.news9),
    path('news10.html', views.news10),
    path('news11.html', views.news11),
    # path('login.html', views.Login),
    path('SignUp', views.SignUp),
    path('LogOut', views.LogOut),
    path('login', views.Login),
    path('loginData', views.loginData),

]
