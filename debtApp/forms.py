from django import forms
from django.contrib.auth.models import User
from debtApp.models import Debt

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length = 100, required = True,
        widget = forms.TextInput(attrs={'class': "form-control"})
    )
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': "form-control"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': 'autofocus',
            'required': 'required', 'placeholder': 'Имя пользователя', 'label': ''})
        self.fields['password'].widget.attrs.update({
            'required': 'required', 'placeholder': 'Пароль', 'label': ''})
    class Meta:
        model = User
        fields = ('username', 'password')
