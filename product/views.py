from django.shortcuts import render
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from product.models import Product


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filters_fields = ("category")
    ordering_fields = ("id", "price")
    search_fields = ("title", "category__title")


class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = "slug"
