from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^add_register/$', views.add_register, name='add_register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^directory/', views.directory, name='directory'),
    #url(r'^directory/(?P<id>[0-9]+)$', views.get_details, name='detail'),
    url(r'^add$', views.add, name='add'),
    url(r'^delete$', views.delete, name='delete'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^logout$', views.logout, name='logout'),
]
