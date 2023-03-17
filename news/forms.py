from .models import News
from django.forms import ModelForm, TextInput, DateInput, TimeInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'anons',
            'text',
            'date',
            'time'
        ]

        widgets = {
            'title': TextInput(attrs={
              'class': 'news-form',
              'placeholder': 'Название'
            }),
            'anons': TextInput(attrs={
              'class': 'news-form',
              'placeholder': 'Анонс'
            }),
            'text': Textarea(attrs={
              'class': 'news-form',
              'placeholder': 'Текст статьи'
            }),
            'date': DateInput(attrs={
              'class': 'news-form',
              'placeholder': 'Дата'
            }),
            'time': TimeInput(attrs={
              'class': 'news-form',
              'placeholder': 'Время'
            }),
        }