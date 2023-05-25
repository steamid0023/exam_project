from requests import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from category.models import Category
from category.serializer import CategorySerializers


class CategoryListCreateApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.order_by("position")
        serializer = CategorySerializers(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
