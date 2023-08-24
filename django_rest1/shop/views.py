from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from kombu.exceptions import OperationalError

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.status import HTTP_200_OK
from django.contrib.auth.views import LoginView

from .models import *
from .forms import *
from .serializers import *
from .service import *
from .tasks import *
from working_with_orders.models import Order_Points


class ProductsListView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/home.html'
    serializer_class = [ProductsListSerializer, CategoryListSerializer]

    def list(self, request, **kwargs):
        products = Products.objects.filter(discount=0)  # товары без скидки
        products_with_discount = Products.objects.filter(discount__gt=0)  # товары со скидкой
        categories = Category.objects.all()
        products_serializer = ProductsListSerializer(products, many=True)
        products_with_discount_serializer = ProductsListSerializer(products_with_discount, many=True)
        category_serializer = CategoryListSerializer(categories, many=True)

        return Response(
            {'products_serializer': products_serializer.data,
             'products_with_discount_serializer': products_with_discount_serializer.data,
             'category_serializer': category_serializer.data,
             }
        )


class ProductDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/product.html'

    def get(self, request, product_slug):
        products = Products.objects.get(slug=product_slug)

        product_serializer = ProductDetailSerializer(products)
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

    def done(self, form_list, **kwargs):
        form1 = form_list[0].cleaned_data
        form2 = form_list[1].cleaned_data
        user = Users.objects.create(
            first_name=form1['first_name'],
            last_name=form1['last_name'],
            username=form1['username'],
            password=make_password(form1['password1']),
            birthday=form1['birthday'],
            email=form2['email'],
            phone=form2['phone'],
            mailing_list=form2['mailing_list'],
            address=form2['address']
        )
        try:
            send_email.delay(form2['email'])
        except OperationalError:
            send(form2['email'])

        return HttpResponseRedirect(reverse('home'))


class SearchProductListView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsListSerializer

    def get_queryset(self):
        self.queryset = self.queryset.filter(product_name__contains=self.request.GET.get('header-search'))
        return self.queryset


def logout_user(request):
    logout(request)
    return redirect('home')


class TestView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/test.html'

    def get(self, request, product_slug):
        products = Products.objects.get(slug=product_slug)
        form = CreateComment()
        day = yesterday()


        product_serializer = ProductDetailSerializer(products)

        return render(request, 'shop/test.html', {'form': form, 'product': product_serializer.data})


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


class ProfileRetrieveAPIView(RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = "slug"


    # check permissions для проверки request
    def check_object_permissions(self, request, obj):

        # print(obj.slug)
        print(obj.slug)
        print(request.user.slug)
        if obj.slug == request.user.slug:
            return True
        else:
            return False




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
