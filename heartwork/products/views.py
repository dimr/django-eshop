from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from models import Product, ProductImage
from rest_framework import generics
from serializers import PicSerializer


class AllProductsView(ListView):
    model = Product
    template_name = "all.html"
    queryset = Product.objects.all().order_by('-updated')
    context_object_name = 'products'




class HomeView(TemplateView):
    template_name = 'home.html'
    model = Product

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {'products': products}
        # return super(HomePageView, self).get(request, *args, **kwargs)
        return self.render_to_response(context)


class SingleProductView(DetailView):
    template_name = 'single.html'
    model = Product
    context_object_name = 'product'
    http_method_names = [u'get']





class PicList(generics.ListAPIView):
    # queryset = ProductImage.objects.all()
    serializer_class = PicSerializer




    def get_queryset(self):
        print self.kwargs
        test = self.kwargs['slug']
        # number = Product.objects.get(slug=test).product_images.all().count()
        # print type(Product.objects.get(slug=test).product_images.all())
        #queryset =  super(PicList,self).get_queryset()
        queryset = Product.objects.get(slug=self.kwargs['slug']).product_images.all()
        return queryset
