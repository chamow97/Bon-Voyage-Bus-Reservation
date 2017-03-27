from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name='home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.UserFormView.as_view(), name='register'),
    url(r'^about$', views.about, name='about'),
    url(r'^booking$', views.booking, name='booking'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

]