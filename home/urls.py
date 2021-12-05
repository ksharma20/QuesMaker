from django.urls.conf import path
from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.ulogin, name='login'),
    path('logout', views.ulogout, name='logout'),
]