from django.db import models
from django.utils.text import slugify

class categories(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="category_pictures", blank=False)

    def get_absolute_url(self):
        return f'/products/'

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name

class products(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="products_pictures", blank=False)
    product_no = models.IntegerField(blank=True, default=0)
    summary = models.TextField(max_length=100, default= "summary")
    products_description = models.TextField(max_length=3000)

    def get_absolute_url(self):
        return f'/products/{self.name}'

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

class product_pictures(models.Model):
    picture = models.ImageField(upload_to = "product_pictures")
    product = models.ForeignKey(products, on_delete = models.CASCADE)

class query(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    query = models.TextField(max_length=1000)

    class Meta:
        verbose_name_plural = "Queries"

    def __str__(self):
        return self.name


class product_images(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="more_product_images")

    class Meta:
        verbose_name_plural = "Product Images"

    def __str__(self):
        return self.product
