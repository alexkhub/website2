from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import *

gender_choices = [
    ('M' , 'муж'),
    ('Ж', 'жен')
]

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'placeholder':"Введите имя"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'placeholder':"Введите пароль"}))

class RegisterForm1(UserCreationForm):


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''




    class Meta:

        model = Users
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2',  'birthday', ]
        widgets ={
            'first_name': forms.TextInput(attrs={'placeholder' :"Введите имя"}),
            'last_name': forms.TextInput(attrs={'placeholder': "Введите фамилию"}),
            'username': forms.TextInput(attrs={'placeholder': "Введите имя пользователя"}),
            'password1': forms.PasswordInput(attrs={'placeholder':"Введите пароль"}),
            'password2': forms.PasswordInput(attrs={'placeholder': "Повторите пароль"}),
            'birthday': forms.DateInput(attrs={ 'placeholder' :"Введите дату рождения"})
        }




class RegisterForm2(forms.ModelForm):


    class Meta:
        model = Users
        fields = ['email', 'phone',  'address', 'mailing_list',]
        widgets={
            'email':forms.EmailInput(attrs={'placeholder':"Введите E-mail"}),
            'phone': forms.TextInput(attrs={'placeholder': "Введите номер телефона"}),
            'address': forms.TextInput(attrs={ 'placeholder' :"Введите ваш адрес"})
        }


class CreateComment(forms.Form):
    # user = forms.CharField(widget=forms.TextInput(attrs={'class' :"field" , 'id': "form-name" , 'placeholder' :"Введите имя и фамилию",  'oninput' :"this.value=this.value.replace(/[^a-zA-Z А-ЯЁа-яё]/g,'')"}))
    rating = forms.IntegerField(widget=forms.TextInput(attrs={'class': "field", 'id': "form-rating", 'placeholder': "Введите вашу оценку (1-10)", 'data-min': "1", 'data-max': "50"}))
    product = forms.IntegerField( widget=forms.TextInput(attrs={'class' :"field", 'id' :"product",    }))


    text = forms.CharField(widget=forms.Textarea(attrs={'id': "form-text", 'cols': "30", 'rows': "10"}))

