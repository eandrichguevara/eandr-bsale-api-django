from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Product

class CategoryView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        categories = list(Category.objects.values())

        categoriesData = []

        for category in categories:
            categoryData = {
                "id": category.id,
                "name": category.name
            }
            categoriesData.append(categoryData)

        if len(categories) > 0:
            data = {'SUCCESS': True, 'CATEGORIES': categoriesData}
            status=200
        else:
            data = {'SUCCESS': False, 'ERROR': 'Categories not found'}
            status=404
            
        response = jsonConfig(data, status)
        return response
    
class ProductView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        products = list(Product.objects.values())

        productsData = []

        for product in products:
            productData = {
                "id": product.id,
                "name": product.name,
                "url_image": product.url_image,
                "price": product.price,
                "discount": product.discount,
            }
            productsData.append(productData)

        if len(products) > 0:
            data = {'SUCCESS': True, 'PRODUCTS': productsData}
            status=200
        else:
            data = {'SUCCESS': False, 'ERROR': 'Products not found'}
            status=404

        response = jsonConfig(data, status)
        return response

class ProductByCategoryView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, category):

        products = list(Product.objects.filter(category_id=category).values())

        productsData = []

        for product in products:
            productData = {
                "id": product.id,
                "name": product.name,
                "url_image": product.url_image,
                "price": product.price,
                "discount": product.discount,
            }
            productsData.append(productData)

        if len(products) > 0:
            data = {'SUCCESS': True, 'PRODUCTS': productData}
            status=200
        else:
            data = {'SUCCESS': False, 'ERROR': 'Products not found'}
            status=404

        response = jsonConfig(data, status)
        return response

class ProductBySearchView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, search):

        products = list(Product.objects.filter(name__icontains = search).values())

        productsData = []

        for product in products:
            productData = {
                "id": product.id,
                "name": product.name,
                "url_image": product.url_image,
                "price": product.price,
                "discount": product.discount,
            }
            productsData.append(productData)

        if len(products) > 0:
            data = {'SUCCESS': True, 'PRODUCTS': productData}
            status=200
        else:
            data = {'SUCCESS': False, 'ERROR': 'Products not found'}
            status=404

        response = jsonConfig(data, status)
        return response

def jsonConfig( data, status ):
    response = JsonResponse(data, status=status)
    response["Content-Type"]                     = "application/json"
    response["Access-Control-Allow-Headers"]     = "X-Requested-With, Content-Type, Authorization, Origin, Accept"
    response["Access-Control-Allow-Origin"]      = "*"
    response["Access-Control-Allow-Credentials"] = "True"
    response["Access-Control-Allow-Methods"]     = "GET, OPTIONS"
    response["Access-Control-Max-Age"]           = "86000"
    return response