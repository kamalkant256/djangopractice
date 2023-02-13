from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Account.models import CustomUser
from django.contrib.auth import authenticate
from Account.serializers import UserLoginSerializer, UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
from rest_framework.permissions import BasePermission, IsAuthenticated





def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }





class UserRegister(APIView):
    def post(self,request):
        # password=request.data['password']
        # user_id=request.data['user_id']
        # username=request.data['username']

        # if user_id:

        #     CustomUser.objects.create(user_id=user_id,password=password,is_superuser=False,first_name="kamal",last_name="kant",username=username,email="kk@gmail.com",is_staff=False,is_active=True,)

        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.data
            get_tokens_for_user(user)
            

            return Response("created successfully")
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserLogin(APIView):
    def post(self,request):
        password=request.data['password']
        user_id=request.data['user_id']
        if user_id and password:
            user=CustomUser.objects.filter(user_id=user_id,password=password).last()
            print(user)
            

            serializer=UserLoginSerializer(user)
            token=get_tokens_for_user(user)
            
            # context=
        
            # return Response("msg":"Login success","userdata":[serializer.data])
            dict = {'user_data':[serializer.data],'token':token,'massage': 'Succesful', 'status': True}

            return Response(dict)
        
class UserProfile(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        # password=request.data['password']
        # user_id=request.data['user_id']
        # if user_id and password:
        user=CustomUser.objects.filter(user_id=request.user.user_id).last()
        print(user)
        

        serializer=UserLoginSerializer(user)
        token=get_tokens_for_user(user)
        
        # context=
    
        # return Response("msg":"Login success","userdata":[serializer.data])
        dict = {'user_data':[serializer.data],'massage': 'Succesful', 'status': True}

        return Response(dict)
        

