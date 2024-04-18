from django.urls import path, include
from . views import UserView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# router = DefaultRouter()

# router.register('api/token', TokenObtainPairView, basename='token_obtain_pair'),
# router.register('api/token/refresh', TokenRefreshView, basename='token_refresh'),
# router.register('api/token/verify', TokenVerifyView, basename='token_verify'),
# router.register('api/user', signup_view, basename='signup'),
# router.register('api/user-detail', User_view, basename='user_detail'),

urlpatterns = [
    # path('', include(router.urls))
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('user/', UserView.as_view({'get': 'list'}), name='user'),
]