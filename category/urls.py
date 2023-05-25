from django.urls import path

from category.views import CategoryListCreateApiView

urlpatterns = [
    path('category/', CategoryListCreateApiView.as_view(), name='category'),
]

