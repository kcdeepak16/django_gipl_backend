from django.shortcuts import render
from .models import categories, products, query
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, 'navbar.html')

def left_dropdown(request):
    return render(request, 'left_dropdown.html')

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def productspage(request):
	if request.is_ajax():
		cat_id = int(request.GET['value'])
		products_list = list(products.objects.filter(category = cat_id).values("id","name","picture","products_description"))
		print(products_list)
		return JsonResponse({'products_list' : products_list})
	categories_list = categories.objects.all()
	return render(request, 'products.html', {'categories_list':categories_list})

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):    return render(request, 'contact_us.html')

@csrf_exempt
def inquiry(request):
	if request.method == "POST":
		current_query = query()
		current_query.name = request.POST.get('name')
		current_query.number = request.POST.get('contact_no')
		current_query.email = request.POST.get('email')
		current_query.query = request.POST.get('message')
		try:
			current_query.save()
			return render(request, 'registered_query.html', {'registered' : True})
		except:
			return render(request, 'registered_query.html', {'registered' : False})
	return render(request, 'inquiry.html', {'products':products.objects.only('name')})		

def products_des(request, name):
	products_info = products.objects.get(name= name)
	print(products_info)
	return render(request, 'product_des.html', {'products_info' : products_info})
