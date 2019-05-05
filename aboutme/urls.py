from django.urls import path
from django.views.generic import TemplateView
from .views import (
    FriendList,
    FriendDetail,
    FriendCreate,
    FriendUpdate,
    FriendDelete,
)

app_name = 'aboutme'
urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='aboutme/zhenglin.html'),
        name='zhenglin'
    ),

    path('aboutme/',
         FriendList.as_view(),
         name='friend_list_urlpattern'),

    path('aboutme/<int:pk>/',
         FriendDetail.as_view(),
         name='friend_detail_urlpattern'),

    path('aboutme/create/',
         FriendCreate.as_view(),
         name='friend_create_urlpattern'),

    path('aboutme/<int:pk>/update',
         FriendUpdate.as_view(),
         name='friend_update_urlpattern'),

    path('aboutme/<int:pk>/delete/',
         FriendDelete.as_view(),
         name='friend_delete_urlpattern'),
]
