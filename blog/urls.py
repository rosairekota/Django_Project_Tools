from django.conf.urls import url
from . import views

urlpatterns=[

	url(r'^$',views.home,name='blog-home'),
	url(r'^lastposts/$',views.lastposts, name='blog-last-post'),
	url(r'^annonement/$',views.annonce, name='blog-post-annonce')
]