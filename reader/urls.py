from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'space/(?P<readerName>\w+)', views.space, name='space'),
        url(r'^loginCheck', views.loginCheck, name='loginCheck'),
        url(r'^login', views.login, name='login'),
        url(r'^logout',views.logout, name='logout'),
        url(r'^registerCheck', views.registerCheck, name='registerCheck'),
        url(r'^register', views.register, name='register'),
        url(r'^profileUpdate', views.profileUpdate, name='profileUpdate'),
        url(r'^profile', views.profile, name='profile'),
        url(r'^passwordUpdate', views.passwordUpdate, name='passwordUpdate'),
        url(r'^uploadIcon', views.uploadIcon, name='uploadIcon'),
        url(r'^updateIcon', views.updateIcon, name='updateIcon'),
]
