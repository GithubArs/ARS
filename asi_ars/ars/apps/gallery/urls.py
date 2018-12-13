from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

app_name = "gallery"

urlpatterns = [
  path('signup/', views.SignUp.as_view(), name='signup'),
  path('update/', views.update, name='update'),
  path('user_timelog/', views.user_timelog, name='user_timelog'),
  path('new/', views.image_create, name='image_new'),
  path('user_acc/', views.user_acc, name='user_acc'),
  path('admin_acc/', views.admin_acc, name='admin_acc'),
  path('timelog/', views.timelog, name='timelog'),
  path('train/', views.train, name='train'),
  path('batchtrain/', views.batchtrain, name='batchtrain'),
  path('edit/<int:pk>', views.image_update, name='image_edit'),
  path('delete/<int:pk>', views.image_delete, name='image_delete'),
  path('move/<int:pk>', views.move, name='move'),
  url(r'^$', views.index, name='index'),
  url(r'^timein/', views.timein, name='timein'),
  url(r'^timeout/', views.timeout, name='timeout'),
  url(r'^snap/', views.snap, name='snap'),
  url(r'^logout/', views.logout, name='logout'),
  url(r'^login/', views.login, name='login'),
  url(r'^reclassify/', views.reclassify, name='reclassify'),
]