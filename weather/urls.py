from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import weather_view

urlpatterns = [
    path('weather/', weather_view, name='weather_view'),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
