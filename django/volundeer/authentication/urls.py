from django.conf.urls import url
from . import views
app_name = 'authentication'

urlpatterns = [
    url(r'^login/', views.login_view, name=''),
    url(r'^register/', views.register_view, name='register'),
]
