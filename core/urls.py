from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name="token_verify"),

    path('api/v1/', include("cars.urls"))
]
