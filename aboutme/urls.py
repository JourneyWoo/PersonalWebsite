from django.urls import path
from django.views.generic import TemplateView

app_name = 'aboutme'
urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='aboutme/zhenglin.html'),
        name='zhenglin'
    ),
]