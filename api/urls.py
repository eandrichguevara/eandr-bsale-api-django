from django.urls import path
from .views import CategoryView, ProductView, ProductByCategoryView, ProductBySearchView

urlpatterns=[
    path('categories/', CategoryView.as_view(), name='categories_list'),
    path('products/', ProductView.as_view(), name='products_list'),
    path('products/category/<int:category>', ProductByCategoryView.as_view(), name='products_by_category_list'),
    path('products/search/<str:search>', ProductBySearchView.as_view(), name='products_by_category_list'),
]