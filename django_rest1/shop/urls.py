from django.urls import path

from .views import *


urlpatterns = [
    path('', ProductsListView.as_view(), name='home'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product'),
    path('comment/', CreateCommentView.as_view(), name='comment'),
    path('test/', TestView.as_view(), name='test')
]