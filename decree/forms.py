from django import forms

from .models import Decrees


class DecreeForm(forms.ModelForm):
    class Meta:
        model = Decrees
        fields = ('type', 'title', 'number', 'file', 'author', 'decree')
        # help_texts = {
        #     'text': 'Текст нового поста',
        #     'group': 'Группа, к которой будет относиться пост'
        # }
        # labels = {
        #     'text': 'Текст поля',
        #     'group': 'Группа'
        # }
