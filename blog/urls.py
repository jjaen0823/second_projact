# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path-converter <type:name>: 지정한 converter type의 name변수를 view 함수로 넘겨라
    path('<int:blog_id>/', views.detail, name = 'detail'),
    path('write/', views.write, name = 'write'),
    path('create', views.create, name = 'create'), # call create function
]