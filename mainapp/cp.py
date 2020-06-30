from .models import categories, products

def return_categories(request):
	names = categories.objects.all()
	cat_list = list(categories.objects.all())
	cat_id = list(categories.objects.only('id'))
	cat_pro = []
	for i in range(1,categories.objects.count()+1):
		cat_current = []
		cat_current.append(cat_list[i-1])
		cat_current.append(list(products.objects.filter(category=cat_id[i-1]).values("name")))
		cat_pro.append(cat_current)
	return {'categories' : cat_pro}