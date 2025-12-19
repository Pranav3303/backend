from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('info/',views.info),
    path('register/',views.tv_reg),
    path('emp/<str:pk>',views.indiv),
    path('update/<str:pk>',views.update),
    path('delete/<str:pk>',views.delete),
    path('tvs/', views.tv_list),
]