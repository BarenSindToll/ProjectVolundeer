from django.conf.urls import url
from . import views
app_name = 'authentication'

urlpatterns = [
    url(r'^login', views.login_user, name='login'),
    url(r'^logout', views.logout_user, name='logout'),
]
