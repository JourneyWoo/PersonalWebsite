from django import forms
from .models import ThoughtsPost


class ThoughtsPostForm(forms.ModelForm):
    class Meta:
        model = ThoughtsPost
        # fields = ('title', 'body', 'tags', 'avatar')
        fields = ('title',)

