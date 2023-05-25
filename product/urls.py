from django.urls import path

from product.views import (
    ProductListCreateApiView, ProductDetailApiView
)

urlpatterns = [
    path("<slug:slug>/", ProductDetailApiView.as_view(), name="product_detail"),
    path("", ProductListCreateApiView.as_view(), name="products_list_create")
]