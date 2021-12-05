from django.urls import path
# from django.conf.urls import url
from . import views

app_name = 'Edit'

urlpatterns = [
    path('', views.index, name='QPAdd'),
    path('/qp/<id>', views.qpedit, name='QPEdit'),
    path('/qp/<id>/ques', views.qpshow, name='QPshow'),
    path('/qp/<id>/delete', views.qpdel, name='QPDel'),
    path('/<id>/ques', views.qadd, name='QAdd'),
    path('/q/<id>', views.qedit, name='QEdit'),
    path('/q/<id>/delete', views.qdel, name='Qdel'),

]
