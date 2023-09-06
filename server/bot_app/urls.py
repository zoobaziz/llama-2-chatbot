from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup', views.singup, name='signup'),
    path('index', views.index, name='index'),
    path('refresh_data', views.refresh_data, name='refresh_data')
]
