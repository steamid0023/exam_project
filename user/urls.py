from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import RegisterView

urlpatterns = [
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='register'),
]