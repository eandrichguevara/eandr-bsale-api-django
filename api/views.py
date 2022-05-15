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

        if len(categories) > 0:
            data = {'SUCCESS': True, 'CATEGORIES': categories}
        else:
            data = {'SUCCESS': False, 'ERROR': 'Categories not found'}
            
        response = jsonConfig(data)
        return response
    
class ProductView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, category=0):

        if (category):
            products = list(Product.objects.filter(category=category).all().values())
        else:
            products = list(Product.objects.all().values())

        if len(products) > 0:
            data = {'SUCCESS': True, 'PRODUCTS': products}
        else:
            data = {'SUCCESS': False, 'ERROR': 'Products not found'}

        response = jsonConfig(data)
        return response

def jsonConfig( data ):
    response = JsonResponse(data)
    response["Content-Type"]                     = "application/json"
    response["Access-Control-Allow-Headers"]     = "X-Requested-With, Content-Type, Authorization, Origin, Accept"
    response["Access-Control-Allow-Origin"]      = "*"
    response["Access-Control-Allow-Credentials"] = "True"
    response["Access-Control-Allow-Methods"]     = "GET, OPTIONS"
    response["Access-Control-Max-Age"]           = "86000"
    return response