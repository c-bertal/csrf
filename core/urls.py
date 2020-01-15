from django.urls import path
from core.views import *


urlpatterns = [
    path('', index, name='index'),
    path('presentation', presentation, name='presentation'),
    path('<int:pk>', view_comment, name='view_comment'),
    path('post_comment', post_comment, name='post_comment'),
    path('save_comment', save_comment, name='save_comment'),
    path('save_comment_post', save_comment_post, name='save_comment_post'),
    path('update_password', update_password, name='save_comment'),

]
