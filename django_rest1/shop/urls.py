from django.urls import path

from .views import *


urlpatterns = [
    path('', ProductsListView.as_view(), name='home'),
    path('show_product/<slug:product_slug>/', ProductDetailView.as_view(), name='show_product'),
    path('login/', Login.as_view(), name='login'),
    path('registration/', RegistrationWizardForm.as_view(), name='registration'),
    path('logout/', logout_user, name='logout'),
    path('add_comment/', add_comment, name='add_comment'),
    path('test/<slug:product_slug>/', TestView.as_view(), name='test'),

]