from django.urls import path
from .views import blog_home,post_detail, post_list,edit_post, delete_post

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('', post_list, name='post_list'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
]


