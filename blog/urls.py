from django.urls import path,re_path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about),
    path('top_search', views.top_search),
    re_path('article/(\d+)/', views.article),
]