from django.urls import path
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "mainapp"

urlpatterns = [
	path('navbar', views.index, name = "navbar"),
    path('', views.home, name = "home"),
    path('products', views.productspage, name = "products"),
    path('about_us', views.about_us, name = "about_us"),
    path('inquiry', views.inquiry, name = "inquiry"),
    path('contact_us', views.contact_us, name = "contact_us"),
    path('products/<str:name>', views.sub_category, name = "subcategory"),
    path('products/<str:sub_category>/<str:name>', views.products_des, name = "products_des"),
    path('test/<str:name>/<str:name2>', views.test, name = "test")
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
