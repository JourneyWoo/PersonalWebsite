from django.contrib import admin
from .models import ThoughtsPost
from .models import ThoughtsColumn

admin.site.register(ThoughtsPost)
admin.site.register(ThoughtsColumn)