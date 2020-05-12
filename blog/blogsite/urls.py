'''
https://www.digitalocean.com/community/tutorials/how-to-enable-and-connect-the-django-admin-interface
'''
from django.urls import path
from . import views
urlpatterns = [
    # path('$/', views.posts, name='posts'),
    # path('$/', views.comments, name='comments'),
    path('', views.index, name='index'),
    path('post/', views.individual_post, name='individual_post')
]