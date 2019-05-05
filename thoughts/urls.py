from django.urls import path
from . import views

app_name = 'thoughts'

urlpatterns = [
    path('thoughts-list/', views.thoughts_list, name='thoughts_list'),
    path('thoughts-detail/<int:id>/', views.thoughts_detail, name='thoughts_detail'),
    path('thoughts-create/', views.thoughts_create, name='thoughts_create'),
    path('thoughts-delete/<int:id>/', views.thoughts_delete, name='thoughts_delete'),
    path('thoughts-update/<int:id>/', views.thoughts_update, name='thoughts_update'),
]