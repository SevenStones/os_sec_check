"""ccv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from ccvapp import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url('^$', views.landing, name="home"),
    url('^windows/$', views.landing),
    url('^ccv/$', views.run_tests),
    url('admin/', admin.site.urls),
    url('^login/', views.login),
    url('logout', views.logout_page),
]
