from http import client
from telnetlib import STATUS
from django.shortcuts import redirect
from .models import User

from rest_framework import generics,viewsets
from .serializers import CustomUserDetailsSerializer, CustomUserRegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.kakao import views as kakao_view

from django.conf import settings
import requests
 
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [IsAuthenticated]
    

class KakaoLoginView(generics.GenericAPIView):
    
    permission_classes=[AllowAny]
    
    def get(self,request,*args, **kwargs):
        client_id = settings.KAKAO_REST_API_KEY
        redirect_uri = settings.KAKAO_REDIRECT_URI
        print(client_id)
        print(redirect_uri)
        return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=account_email")

class KakaoCallbackView(generics.GenericAPIView):
    
    permission_classes=[AllowAny]
    
    def get(self, request, *args, **kwargs):
        code = self.request.GET.get("code")
        client_id = settings.KAKAO_REST_API_KEY
        redirect_uri = settings.KAKAO_REDIRECT_URI
        BASE_URL = settings.BASE_URL
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
        )
        token_json = token_request.json()
        print(token_json)
        access_token = token_json.get("access_token")
        profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"})
        profile_json = profile_request.json()
        print(profile_json)
        # print(access_token)
        data = {'access_token': access_token, 'code': code}
        # print(data)
        accept = requests.post(
            f"{BASE_URL}login/kakao/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            print(accept_status)
            return Response({'err_msg': 'failed to signin'}, status=accept_status)
        accept_json = accept.json()
        return Response(accept_json)
    
class KakaoLoginToDjango(SocialLoginView):
    
    permission_classes=[AllowAny]
    
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = settings.KAKAO_REDIRECT_URI