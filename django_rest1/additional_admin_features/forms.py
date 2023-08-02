from django import forms

class MailingForm(forms.Form):
    mail_text = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'cols': 60, 'row': 10}))

