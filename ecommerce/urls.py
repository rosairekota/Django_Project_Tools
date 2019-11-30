"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .import views
from users_app import views as user_views

urlpatterns = [
	url(r'^$',views.home_page, name='home-project'),
	url(r'^about/$',views.about_page, name='about_project'),
	url(r'^contact/$',views.contact_page, name='contact_project'),
     # Users app- In the Parent project
	url(r'^register/$', user_views.register, name='user-register'),
    url(r'^profile/$', user_views.profile, name='user-profile'),
    url(r'^login/$', auth_views.login, {'template_name': 'users/login.html'}, name='user-login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'users/logout.html'}, name='user-logout'),
    url(r'^blog/',include('blog.urls')),
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns=urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

