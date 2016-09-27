from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from django.contrib.auth.views import login,logout_then_login

app_name = 'home'
urlpatterns = [

    url(r'^$', login ,{'template_name':'home/login1.html'}, name='login1'),

    url(r'^home/$',login_required(views.HomeView.as_view()), name='home'),

    url(r'^registrar/$', views.RegistrarUsuario.as_view(), name='registrar'),

    url(r'^logout/', logout_then_login, name='logout'),

    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detail'),

    url(r'pote/add/$', login_required(views.PoteCreate.as_view()), name='pote-add'),

]