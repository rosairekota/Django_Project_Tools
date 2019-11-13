from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .import views as user_views

urlpatterns = [
	url(r'^register/$', user_views.register, name='user-register'),
	url(r'^profile/$', user_views.profile, name='user-profile'),
	url(r'^login/$', auth_views.login, {'template_name': 'users/login.html'}, name='user-login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'users/logout.html'}, name='user-logout'),

	
] 
#url(r'^$', views.home), url(r'^login/$', auth_views.login, {'template_name': 'useraccounts/login.html'}, name='login')