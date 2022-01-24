from http import client
from os import access
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
from dj_rest_auth.views import LogoutView, LoginView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
# from core.models import Outstanding
from rest_framework import status
from django.utils.translation import gettext as _
import jwt
from allauth.account.adapter import get_adapter
from allauth.socialaccount.models import SocialAccount
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout as django_logout
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q

from dj_rest_auth.jwt_auth import unset_jwt_cookies

from django.conf import settings
import requests
 
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserDetailsSerializer
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
        email = profile_json['kakao_account'].get('email')
        try:
            user = User.objects.get(email=email)
            # 기존에 가입된 유저의 Provider가 kakao가 아니면 에러 발생, 맞으면 로그인
            # 다른 SNS로 가입된 유저
            social_user = SocialAccount.objects.get(user=user)
            if social_user is None:
                return Response({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)
            if social_user.provider != 'kakao':
                return Response({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)
            # 기존에 Google로 가입된 유저
            print(user.__dict__)
            
            self.update_blanked_list(user.pk)
            
            data = {'access_token': access_token, 'code': code}
            accept = requests.post(
                f"{BASE_URL}login/kakao/finish/", data=data)
            accept_status = accept.status_code
            if accept_status != 200:
                return Response({'err_msg': 'failed to signin'}, status=accept_status)
            accept_json = accept.json()
            response = Response(accept_json)
            response.set_cookie('access_token', accept_json['access_token'], httponly=True)
            # accept_json.pop('user', None)
            return response
        except User.DoesNotExist:
            data = {'access_token': access_token, 'code': code}
            accept = requests.post(
                f"{BASE_URL}login/kakao/finish/", data=data)
            accept_status = accept.status_code
            if accept_status != 200:
                return Response({'err_msg': 'failed to signup'}, status=accept_status)
            # user의 pk, email, first name, last name과 Access Token, Refresh token 가져옴
            accept_json = accept.json()
            response = Response(accept_json)
            response.set_cookie('access_token', accept_json['access_token'], httponly=True)
            # accept_json.pop('user', None)
            return response
        
    def update_blanked_list(self,user_id):
        blank_listed = BlacklistedToken.objects.select_related('token').values('token_id')
        if user_id is not None:
            token_info = OutstandingToken.objects.filter(Q(user=user_id) & ~Q(pk__in=blank_listed)).values()
            print('token_info')
            print(token_info)
            for info in token_info:
                print(info)
                token = RefreshToken(info['token'])
                token.blacklist()
    
class KakaoLoginToDjango(SocialLoginView):
    
    permission_classes=[AllowAny]
    
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = settings.KAKAO_REDIRECT_URI
        

class Logout(LogoutView):
    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        if getattr(settings, 'REST_SESSION_LOGIN', True):
            django_logout(request)

        response = Response(
            {'detail': 'Successfully logged out.'},
            status=status.HTTP_200_OK,
        )

        if getattr(settings, 'REST_USE_JWT', False):
            # NOTE: this import occurs here rather than at the top level
            # because JWT support is optional, and if `REST_USE_JWT` isn't
            # True we shouldn't need the dependency
            cookie_name = getattr(settings, 'JWT_AUTH_COOKIE', None)
            print(response.__dict__)
            unset_jwt_cookies(response)
            print(0)
            print(response.__dict__)
            if 'rest_framework_simplejwt.token_blacklist' in settings.INSTALLED_APPS:
                print(1)
                # add refresh token to blacklist
                try:
                    access_token = request.data['access_token']
                    info = jwt.decode(access_token,options={"verify_signature": False})
                    blank_listed = BlacklistedToken.objects.select_related('token').values('token_id')
                    token_info = OutstandingToken.objects.filter(Q(user=info["user_id"]) & ~Q(pk__in=blank_listed)).values()
                    for info in token_info:
                        token = RefreshToken(info['token'])
                        token.blacklist()
                except KeyError:
                    response.data = {'detail': _('Refresh token was not included in request data.')}
                    response.status_code =status.HTTP_401_UNAUTHORIZED
                except (TokenError, AttributeError, TypeError) as error:
                    if hasattr(error, 'args'):
                        if 'Token is blacklisted' in error.args or 'Token is invalid or expired' in error.args:
                            response.data = {'detail': _(error.args[0])}
                            response.status_code = status.HTTP_401_UNAUTHORIZED
                        else:
                            response.data = {'detail': _('An error has occurred.')}
                            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

                    else:
                        response.data = {'detail': _('An error has occurred.')}
                        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

            elif not cookie_name:
                message = _(
                    'Neither cookies or blacklist are enabled, so the token '
                    'has not been deleted server side. Please make sure the token is deleted client side.',
                )
                response.data = {'detail': message}
                response.status_code = status.HTTP_200_OK
        return response