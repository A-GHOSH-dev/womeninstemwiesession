from django.contrib import admin
from django.urls import path, include
from womeninstem import views

#admin.site.site_header ="Developer Ananya Ghosh"
#admin.site.site_title= "Welcome to my dashboard"
#admin.site.index_title="Welcome to my portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    #path('home', views.home, name='home'),
    #path('signup', views.signup, name='signup'),
    #path('signup', views.handleSignup, name='handleSignup'),
    #path('login', views.handleLogin, name='handleLogin'),
    #path('logout', views.handleLogout, name='handleLogout'),
    path('womeninstem', views.womeninstem, name='womeninstem'),
    path('form', views.form, name='form'),
    path('sharestory', views.sharestory, name='sharestory'),
    path('seestory', views.seestory, name='seestory'),


]

