from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:postId>/', views.detail, name='detail'),
    path('answer/create/<int:postId>/', views.answer_create, name='answer_create'),
    path('addpost/', views.addpostmove, name='addpostmove'),
    path('post_new/', views.post_new_modelform, name='post_new_modelform'),
    path('post_edit/<int:pk>', views.post_edit, name='post_edit'),
    path('post_edit_form/<int:pk>', views.post_edit_form, name='post_edit_form'),
    path('post_remove/<int:pk>', views.post_remove, name='post_remove'),

]

