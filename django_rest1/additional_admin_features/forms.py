from django import forms

class MailingForm(forms.Form):
    username = forms.CharField(label="Никнейм")
    email = forms.EmailField(label='Почта')
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'cols': 60, 'row': 10}))