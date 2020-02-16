from django.urls import path, include
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.SearchPostsView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('search/', views.SearchPostsView.as_view(), name='search_posts'),
]
