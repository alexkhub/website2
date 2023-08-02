from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test, login_required

from .forms import *
from .service import *
from shop.models import Users

# Create your views here.

@user_passes_test(lambda u: u.is_staff)
def index(request):
    # if request.user.is_staff:
    #     return render(request, 'additional_admin_features/main_page.html')
    # else:
    #     return HttpResponseRedirect(reverse('home'))
    return render(request, 'additional_admin_features/main_page.html')

class MailingForm(UserPassesTestMixin, FormView):
    form_class = MailingForm
    template_name = 'additional_admin_features/mailing.html'
    success_url = reverse_lazy('additional_admin_features')

    def test_func(self):
        if self.request.user.is_staff:
            return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('aaf_mailing')

    def form_valid(self, form):
        clean_form = form.cleaned_data
        mail_text = clean_form['mail_text']
        users = Users.objects.filter(mailing_list=True)
        for user in users:
            send(mail_text=mail_text, user_email=user.email)

        return super(MailingForm, self).form_valid(form)
