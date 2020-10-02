from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from mainapp.models import *

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['mainapp:home','mainapp:products','mainapp:about_us','mainapp:inquiry','mainapp:contact_us']

    def location(self, item):
        return reverse(item)

class CategoryView(Sitemap):

    def items(self):
        return categories.objects.all()

class ProductView(Sitemap):

    def items(self):
        return products.objects.all()