from django.urls import re_path
from app import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category')
]