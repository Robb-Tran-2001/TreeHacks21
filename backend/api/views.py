from django.shortcuts import render
from rest_framework import generics, status
from .models import User, Image
from .serializers import UserSerializer, CreateUserSerializer, ImageSerializer, CreateImageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

#Each view is associated with a model and a serializer
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#users stored and identified by their unique session(id)
class CreateUserView(APIView):
    serializer_class = CreateUserSerializer
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session._session_key):
            #if user does not have unique session
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        #check if fields in request are valid
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            queryset = User.objects.filter(username=username)
            if not queryset.exists():
                user = User(username=username, password=password)
                user.save()
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response({"success": "no"}, status=status.HTTP_409_CONFLICT)


class LoginUserView(APIView):
    serializer_class = CreateUserSerializer
    def post(self, request, format=None):
        username=self.request.data['username']
        password=self.request.data['password']
        queryset = User.objects.filter(username=username, password=password)
        if queryset.exists():
            user = User(username=username, password=password)
            return Response(UserSerializer(user).data, status=status.HTTP_202_ACCEPTED)
        return Response({"success": "no"}, status=status.HTTP_401_UNAUTHORIZED)

class ImageView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class CreateImageView(APIView):
    serializer_class = CreateImageSerializer
    def post(self, request, format=None):
        print(request.data)
        filename = request.data['image']
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            image_path = './media/images/'+str(filename)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        