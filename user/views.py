from drf_yasg.utils import swagger_auto_schema
from requests import Response
from rest_framework import status
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.views import APIView

from user.models import User
from user.serializer import RegisterSerializer


class RegisterView(APIView):
    queryset = User.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
