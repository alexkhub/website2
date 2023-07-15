from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from formtools.wizard.views import SessionWizardView

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.status import HTTP_200_OK
from django.contrib.auth.views import LoginView


from .models import *
from .forms import *
from .serializers import *



class ProductsListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/home.html'

    def get(self, request):
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


class CreateCommentView(APIView):

    def post(self, request):
        serializer = CreateCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    # def put(self, request, id=None ):
    #     comment = Comments.objects.filter(id=id)
    #     serializer = CreateCommentSerializer(comment, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Login(LoginView):

    form_class = LoginForm
    template_name = 'shop/login.html'

    def get_success_url(self):
        return reverse_lazy('home')



class RegistrationWizardForm(SessionWizardView):
    form_list = [RegisterForm1, RegisterForm2]
    template_name = 'shop/register_step1.html'
    success_url = reverse_lazy('home')

    def done(self, form_list,  **kwargs):
        form1 = form_list[0].cleaned_data
        form2 = form_list[1].cleaned_data
        user = Users.objects.create(
            first_name=form1['first_name'],
            last_name=form1['last_name'],
            username =form1['username'],
            password = form1['password1'],
            gender = form1['gender'],
            birthday = form1['birthday'],
            email = form2['email'],
            phone = form2['phone'],
            mailing_list = form2['mailing_list'],
            address = form2['address']
        )
        return HttpResponseRedirect(reverse('home'))







class TestView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/product.html'

    def get(self, request, product_slug):
        products = Products.objects.get(slug=product_slug)

        product_serializer = TestSerializer(products)
        return Response({'product': product_serializer.data})
