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

    path('friendcircle/',
         FriendList.as_view(),
         name='friend_list_urlpattern'),

    path('friendcircle/<int:pk>/',
         FriendDetail.as_view(),
         name='friend_detail_urlpattern'),

    path('friendcircle/create/',
         FriendCreate.as_view(),
         name='friend_create_urlpattern'),

    path('friendcircle/<int:pk>/update',
         FriendUpdate.as_view(),
         name='friend_update_urlpattern'),

    path('friendcircle/<int:pk>/delete/',
         FriendDelete.as_view(),
         name='friend_delete_urlpattern'),

    path('contact', TemplateView.as_view(template_name='aboutme/contact.html'), name='contactme'),

    path('whyiamhere', TemplateView.as_view(template_name='aboutme/whyiamhere.html'), name='whyiamhere'),

    path('intro', TemplateView.as_view(template_name='aboutme/intro.html'), name='intro'),
]
