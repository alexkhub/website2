from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

class RegisterForm1(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''


    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'gender', 'birthday', ]



class RegisterForm2(forms.ModelForm):
    # email = forms.EmailField(label='Почта', widget=forms.EmailField())
    # phone = forms.CharField(label='Номер телефона', widget=forms.TextInput())
    # mailing_list = forms.BooleanField(label='Разрешить отправлять сообщения', widget=forms.CheckboxInput())
    # address = forms.CharField(label='Адрес', widget=forms.TextInput())
    class Meta:
        model = Users
        fields = ['email', 'phone', 'mailing_list', 'address']





