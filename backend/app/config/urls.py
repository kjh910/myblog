"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularJSONAPIView,SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import include

from users import views as users_views

from rest_framework import routers
from users.views import CustomUserViewSet
from contents.views import ContentsViewSet, CategoriesViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register(r'user', CustomUserViewSet)
router.register(r'contents', ContentsViewSet)
router.register(r'categories', CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += [
    path('', include('dj_rest_auth.urls')),
    # path('login/test/', users_views.Login().as_view(), name="login"),
    path('logout/test/', users_views.Logout().as_view(), name="logout"),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('/social/', include('allauth.urls')),
]

urlpatterns += [
    path('login/kakao/', users_views.KakaoLoginView().as_view(), name="kakao-login"),
    path('login/kakao/callback/', users_views.KakaoCallbackView().as_view(), name="kakao-callback"),
    path('login/kakao/finish/', users_views.KakaoLoginToDjango().as_view(), name="kakao-finish")
]

urlpatterns += [
    path("api/docs/json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
