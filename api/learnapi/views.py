from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BlogSerializer
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes,permission_classes
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

# Create your views here.

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

@api_view(['GET', 'POST', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api(request):
    
        
    if(request.method=='GET'):
        blog=Blogpost.objects.all()
        d=BlogSerializer(blog,many=True)
        return Response(d.data)
    if(request.method=='POST'):
        print(request.data)

        # user=request.data['username']
        # t=Token.objects.create(user=user)
        # print(t.key)
        c=BlogSerializer(data=request.data)
        
        if c.is_valid():
            c.save()
            print(c.data)
            return Response(c.data,status=status.HTTP_201_CREATED)

   
    return render(request,'index.html')


@api_view(['PUT','GET'])
def pu(request,pk):
    if(request.method=='GET'):
        blog=Blogpost.objects.all()
        d=BlogSerializer(blog,many=True)
        return Response(d.data)
    try: 
        tutorial = Blogpost.objects.get(pk=pk) 
    except tutorial.DoesNotExist: 
        return Response({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method=="PUT":
        serializer =BlogSerializer(tutorial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request,'index.html')



