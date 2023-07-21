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

    class Meta:
        model = Users
        fields = ['email', 'phone', 'mailing_list', 'address']

class CreateComment(forms.Form):
    # user = forms.CharField(widget=forms.TextInput(attrs={'class' :"field" , 'id': "form-name" , 'placeholder' :"Введите имя и фамилию",  'oninput' :"this.value=this.value.replace(/[^a-zA-Z А-ЯЁа-яё]/g,'')"}))
    rating = forms.IntegerField(widget=forms.TextInput(attrs={'class': "field", 'id': "form-rating", 'placeholder': "Введите вашу оценку (1-10)", 'data-min': "1", 'data-max': "50"}))
    product = forms.IntegerField( widget=forms.TextInput(attrs={'class' :"field", 'id' :"product",    }))


    text = forms.CharField(widget=forms.Textarea(attrs={'id': "form-text", 'cols': "30", 'rows': "10"}))

