from django.conf.urls import url
from . import views
from .views import (
	PostListView,
	PostDetailView,
	)

urlpatterns=[

	url(r'^$',PostListView.as_view(), name='blog-home'),
	url(r'^post/$',PostDetailView.as_view(), name='blog-post-detail'),
	url(r'^lastposts/$',views.lastposts, name='blog-last-post'),
	url(r'^annonement/$',views.annonce, name='blog-post-annonce')
]