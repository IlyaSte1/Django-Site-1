from .models import Register
from django.forms import TextInput, ModelForm


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = [
            'log_in',
            'password'
        ]

        widgets = {
            'log_in': TextInput(attrs={
                'class': 'reg-window',
                'placeholder': 'Логин'
            }),
            'password': TextInput(attrs={
                'class': 'reg-window',
                'placeholder': 'Пароль'
            }),
        }