import logging
import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import Q, Prefetch
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from kombu.exceptions import OperationalError
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
from rest_framework.renderers import TemplateHTMLRenderer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.views import LoginView
from .models import *
from .forms import *
from .serializers import *
from .service import *
from .tasks import *
from .permissions import ProfilePermission
from working_with_orders.models import Order_Points, Orders
from working_with_orders.serializers import OrderSerializer

logger = logging.getLogger(__name__)


class ProductsListView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/home.html'

    # @method_decorator(cache_page(30))
    # @method_decorator(vary_on_headers("Home", ))
    def list(self, request, **kwargs):
        products = Products.objects.filter(Q(discount=0) & Q(numbers__gt=0)).prefetch_related(
            Prefetch('product_photos', queryset=Product_Images.objects.filter(first_img=True))).only(
            'id', 'numbers', 'product_photos', 'discount', 'product_name', 'last_price', 'slug')  # товары без скидки

        products_with_discount = Products.objects.filter(Q(discount__gt=0) & Q(numbers__gt=0)).prefetch_related(
            Prefetch('product_photos', queryset=Product_Images.objects.filter(first_img=True))).only(
            "id", 'numbers', 'product_photos', 'discount', 'product_name', 'last_price', 'slug')  # товары со скидкой

        categories = get_categories()
        manufacturer = get_manufacturers()
        manufacturer_serializer = ManufacturerSerializer(manufacturer, many=True)
        products_serializer = HomeProductsListSerializer(products, many=True)
        products_with_discount_serializer = HomeProductsListSerializer(products_with_discount, many=True)
        category_serializer = CategoryListSerializer(categories, many=True)

        return Response(
            {'products_serializer': products_serializer.data,
             'products_with_discount_serializer': products_with_discount_serializer.data,
             'category_serializer': category_serializer.data,
             'manufacturer_serializer': manufacturer_serializer.data
             }
        )


class ProductRetrieveView(RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/product.html'
    lookup_field = "slug"
    queryset = Products.objects.prefetch_related(
        Prefetch('manufacturer', queryset=Manufacturer.objects.all().only('manufacturer_name')),
        Prefetch('category', queryset=Category.objects.all().only('name')),
        Prefetch('comments', queryset=Comments.objects.all().prefetch_related(
            Prefetch('user', queryset=Users.objects.all().only('username'))
        )),
    ).only(
        'id', 'numbers', 'manufacturer', 'product_photos', 'category', 'discount',
        'product_name', 'last_price', 'description', 'first_price', 'slug')
    serializer_class = ProductDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        product_serializer = self.get_serializer(self.get_object())
        return Response({'product': product_serializer.data})


class Login(LoginView):
    form_class = LoginForm
    template_name = 'shop/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class RegistrationWizardForm(SessionWizardView):
    form_list = [RegisterForm1, RegisterForm2]
    template_name = 'shop/register_step1.html'
    success_url = reverse_lazy('home')
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'user_photo'))

    def done(self, form_list, **kwargs):
        form1 = form_list[0].cleaned_data
        form2 = form_list[1].cleaned_data
        # processed_image = update_photo(form2['user_photo'])

        user = Users.objects.create(
            first_name=form1['first_name'],
            last_name=form1['last_name'],
            username=form1['username'],
            password=make_password(form1['password1']),
            birthday=form1['birthday'],
            email=form2['email'],
            phone=form2['phone'],
            mailing_list=form2['mailing_list'],
            address=form2['address'],
            user_photo=form2['user_photo']

        )
        try:
            send_email.delay(form2['email'])
        except OperationalError:
            logger.critical('sending email is suspended')

            Emails.objects.create(
                email=form2['email']
            )
        login(self.request, user)
        return HttpResponseRedirect(reverse('home'))


class SearchProductListView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/catalog.html'

    queryset = Products.objects.filter(numbers__gt=0).prefetch_related(
        Prefetch('product_photos', queryset=Product_Images.objects.filter(first_img=True)),
        Prefetch('manufacturer', queryset=Manufacturer.objects.all().only('slug')),
        Prefetch('category', queryset=Category.objects.all().only('slug'))
    ).only(
        'id', 'numbers', 'manufacturer', 'product_photos', 'category', 'discount',
        'product_name', 'last_price', 'slug')

    serializer_class = ProductsListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        self.queryset = self.queryset.filter(product_name__contains=self.request.GET.get('header-search'))
        return self.queryset

    @method_decorator(cache_page(60 * 30))
    @method_decorator(vary_on_headers("SearchProducts", ))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer_products = self.get_serializer(queryset, many=True)

        return Response({'products': serializer_products.data})


class CatalogListView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/catalog.html'

    queryset = Products.objects.filter(numbers__gt=0).prefetch_related(
        Prefetch('product_photos', queryset=Product_Images.objects.filter(first_img=True)),
        Prefetch('manufacturer', queryset=Manufacturer.objects.all().only('slug')),
        Prefetch('category', queryset=Category.objects.all().only('slug', 'name'))
    ).only(
        'id', 'numbers', 'manufacturer', 'product_photos', 'category', 'discount',
        'product_name', 'last_price', 'slug')

    serializer_class = ProductsListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    # @method_decorator(cache_page(60 * 30))
    # @method_decorator(vary_on_headers("CatalogProducts", ))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        categories = get_categories()
        manufacturer = get_manufacturers()
        serializer_products = self.get_serializer(queryset, many=True)
        manufacturer_serializer = ManufacturerSerializer(manufacturer, many=True)
        category_serializer = CategoryListSerializer(categories, many=True)

        return Response({'products': serializer_products.data,
                         'categories': category_serializer.data,
                         'manufacturers': manufacturer_serializer.data
                         }
                        )


class ProfileRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'shop/profile.html'
    queryset = Users.objects.all().only('id', 'first_name', 'password', 'last_name',
                                        'username', 'date_joined', 'phone', 'slug', 'address', 'user_photo')
    serializer_class = UserSerializer
    lookup_field = "slug"
    permission_classes = (ProfilePermission,)

    def retrieve(self, request, *args, **kwargs):
        user_profile = self.get_object()
        unpaid = Orders.objects.filter(Q(user=request.user) & Q(paid_order=False) & Q(delivery=False))
        paid = Orders.objects.filter(Q(user=request.user) & Q(paid_order=True))
        delivery = Orders.objects.filter(Q(user=request.user) & Q(delivery=True))

        unpaid_serializer = OrderSerializer(unpaid, many=True)
        paid_serializer = OrderSerializer(paid, many=True)
        delivery_serializer = OrderSerializer(delivery, many=True)

        user_serializer = self.get_serializer(user_profile)

        return Response(
            {
                'unpaid_orders': unpaid_serializer.data,
                'paid_orders': paid_serializer.data,
                'delivery_orders': delivery_serializer.data,
                'profile': user_serializer.data
            }
        )

    def patch(self, request, *args, **kwargs):

        return self.partial_update(request, *args, **kwargs)


class CategoryListAPIView(ListAPIView):
    queryset = Products.objects.filter(numbers__gt=0).prefetch_related(
        Prefetch('product_photos', queryset=Product_Images.objects.filter(first_img=True)),
        Prefetch('manufacturer', queryset=Manufacturer.objects.all().only('slug')),
        Prefetch('category', queryset=Category.objects.all().only('slug', 'name'))
    ).only(
        'id', 'numbers', 'manufacturer', 'product_photos', 'category', 'discount',
        'product_name', 'last_price', 'slug')

    serializer_class = ProductsListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter

    def get_queryset(self):
        self.queryset = self.queryset.filter(category__slug=self.request.resolver_match.kwargs['category_slug'])
        return self.queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer_products = self.get_serializer(queryset, many=True)
        # return Response({'products': serializer_products.data})
        return Response(serializer_products.data)


class ManufacturerListAPIView(ListAPIView):
    queryset = Products.objects.filter(numbers__gt=0).prefetch_related(
        Prefetch('product_photos', queryset=Product_Images.objects.filter(first_img=True)),
        Prefetch('manufacturer', queryset=Manufacturer.objects.all().only('slug')),
        Prefetch('category', queryset=Category.objects.all().only('slug')))
    serializer_class = ProductsListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ManufactureFilter

    def get_queryset(self):
        self.queryset = self.queryset.filter(manufacturer__slug=self.request.resolver_match.kwargs['manufacturer_slug'])
        return self.queryset

    @method_decorator(cache_page(60 * 30))
    @method_decorator(vary_on_headers("ManufacturerProducts", ))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer_products = self.get_serializer(queryset, many=True)
        # return Response({'products': serializer_products.data})
        return Response(serializer_products.data)


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def add_comment(request):
    if request.POST:

        form = CreateComment(request.POST)
        url = request.META.get('HTTP_REFERER')
        if form.is_valid():
            user = request.user
            rating = form.data['rating']
            product_1 = int(form.data['product'])
            product = Products.objects.get(id=product_1)
            text = form.data['text']
            comment = Comments.objects.create(
                user=user,
                rating=rating,
                product=product,
                text=text
            )

        return redirect(url)


@login_required(login_url='login')
def add_product(request, id):
    url = request.META.get('HTTP_REFERER')
    product = Products.objects.get(id=id)
    user = request.user
    if not Order_Points.objects.filter(user=user, product=product, in_orders=False):
        Order_Points.objects.create(
            user=user,
            product=product
        )
        return redirect(url)
    else:
        return redirect('basket')


def tr_handler500(request):
    """Обработка ошибки 500"""
    return render(request=request, template_name='shop/error_page.html', status=500, context={
        'title': 'Ошибка сервера: 500',
        'error_message': 'Внутренняя ошибка сайта, вернитесь на главную страницу, отчет об ошибке мы направим '
                         'администрации сайта',
    })


def tr_handler403(exc, context):
    """Обработка ошибки 403"""
    if isinstance(exc, PermissionDenied):
        return render(context['request'], template_name='shop/error_page.html', status=403, context={
            'title': 'Ошибка доступа: 403',
            'error_message': 'Доступ к этой странице ограничен',
        })

    response = exception_handler(exc, context)
    return response


def tr_handler404(request, exception):
    """ Обработка ошибки 404"""
    return render(request=request, template_name='shop/error_page.html', status=404, context={
        'title': 'Страница не найдена: 404',
        'error_message': 'К сожалению такая страница была не найдена, или перемещена',
    })

# class ProfileViewSet(ModelViewSet):
#     # renderer_classes = [TemplateHTMLRenderer]
#     # template_name = 'shop/profile.html'
#     queryset = Users.objects.all().only('id', 'first_name', 'password', 'last_name',
#                                         'username', 'date_joined', 'phone', 'slug', 'address', 'user_photo')
#     serializer_class = UserSerializer
#     lookup_field = "slug"
#     permission_classes = (ProfilePermission,)
#
#     def retrieve(self, request, *args, **kwargs):
#         user_profile = self.get_object()
#         unpaid = Orders.objects.filter(Q(user=request.user) & Q(paid_order=False) & Q(delivery=False))
#         paid = Orders.objects.filter(Q(user=request.user) & Q(paid_order=True))
#         delivery = Orders.objects.filter(Q(user=request.user) & Q(delivery=True))
#
#         unpaid_serializer = OrderSerializer(unpaid, many=True)
#         paid_serializer = OrderSerializer(paid, many=True)
#         delivery_serializer = OrderSerializer(delivery, many=True)
#
#         user_serializer = self.get_serializer(user_profile)
#
#         return Response(
#             {
#                 'unpaid_orders': unpaid_serializer.data,
#                 'paid_orders': paid_serializer.data,
#                 'delivery_orders': delivery_serializer.data,
#                 'profile': user_serializer.data
#             }
#         )
#
#     def patch(self, request, *args, **kwargs):
#         if (request.data['email'] == request.data['reenter_email']) and (request.data['reenter_email'] != '') and (
#                 check_password(request.data['last_password'], request.user.password) and (
#                 request.data['password'] != '') and (
#                         request.data['password'] == request.data['reenter_password']
#                 )):
#             request.data['password'] = make_password(request.data['password'])
#         return self.partial_update(request, *args, **kwargs)
#
#         else:
#
#         messages.error(request, 'Ошибка заполнения полей')
