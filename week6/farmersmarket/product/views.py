from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

def show_all_products(request):
    products = Product.objects.all()
    # return HttpResponse('<h1>Display All Available Products</h1>')
    context = {'displayProducts' : products}
    return render(request, 'product/index.html', context)

def show_category_products(request, catname):
    try:
        products = Product.objects.filter(categoryid__name__iexact = catname)
        # print(products.query)

        # for product in products:
        #     print(product)
        if products.count() > 0:
            # return HttpResponse(f'<h1>Display all products of the {catname} type')
            context = {'displayProducts' : products, 'categoryName' : catname}
            return render(request, 'product/index.html', context)
        else:
            return HttpResponse(f'<h1>Unable to locate any items in our datebase of type {catname}')
    except:
        return HttpResponse(f'<h1>Unable to locate any producuts of {catname}')

def show_product(request, proid):
    try:
        product = Product.ojects.get(id=proid)
        # return HttpResponse(f'<h1>Showing more details for "{product}"</h1>')
        return render(request, 'product/index.html', {'displayProduct' : product})
    except Product.DoesNotExist:
        return HttpResponse(f'<h1>Unable to locate product whose id is {proid}')

