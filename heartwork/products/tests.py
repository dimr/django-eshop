from django.test import TestCase, Client, RequestFactory
from selenium import webdriver
# Create your tests here.
from models import Product
from django.core.urlresolvers import resolve



class ProductTestCase(TestCase):
    def index(self):
        pass

    def setUp(self):
        self.factory=RequestFactory()
        Product.objects.create(title='testProduct', price=23, sales_price=100)


    def test_products(self):
        p = Product.objects.get(title='testProduct')
        self.assertEqual(p.title, 'testProduct')
        self.assertEqual(p.price, 23)
        self.assertEqual(p.sales_price, 100)
