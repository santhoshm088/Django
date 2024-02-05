from django.contrib import admin
from django.urls import path, include
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.home,name="home"),
    
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    # path('ok',views.first),
    path('activate/<uidb64>/<token>',views.activate,name="activate"),
    path('videohome',views.videohome,name="videohome"),
    path('complaint',views.complaint,name="complaint"),
    path('student',views.student,name="student"),
    path('update_complaint',views.update_complaint,name="update_complaint")
]

urlpatterns +=staticfiles_urlpatterns()