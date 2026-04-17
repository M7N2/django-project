# Defines URL schemes for blogs.
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page (last 4 posts).
    path('', views.index, name='index'),
    # All posts page.
    path('all/', views.all_posts, name='all_posts'),
    # New message page.
    path('create/', views.create_post, name='new_post'),
    # Message editing page.
    path('edit/<int:post_id>/', views.edit_post, name='edit'),
    # View single post page.
    path('post/<int:post_id>/', views.view_post, name='post'),
    # Delete post.
    path('delete/<int:post_id>', views.delete_post, name='delete'),
]
