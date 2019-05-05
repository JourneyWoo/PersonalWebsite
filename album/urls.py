from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'album'
urlpatterns = [
    path('album_list/', views.AlbumListView.as_view(), name='album_list'),
    path('manage/', views.album_manage, name='album_manage'),
    path('upload/', views.AlbumUpload.as_view(), name='album_upload'),
    url(r'^delete/(?P<image_id>\d+)/$', views.album_delete, name='album_delete'),
    #path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
]
