from django.shortcuts import render
from rest_framework import generics, status
from .models import User, Image
from .serializers import UserSerializer, CreateUserSerializer, ImageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .block import Block
from .blockchain import Blockchain

bc = Blockchain()

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
    serializer_class = ImageSerializer
    def post(self, request, format=None):
        filename = request.data['image']
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            image_path = './media/'+str(filename)
            matches = bc.search(image_path)
            if len(matches) is 0:
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(matches, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateImageView(APIView):
    serializer_class = ImageSerializer
    def post(self, request, format=None):
        print(request.data['image'])
        filename = request.data['image']
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            image_path = './media/'+str(filename)
            serializer.save()
            #get block from mining
            b = bc.mine(image_path)
            if b is not None:
                hash_div = b.get_hash_div()
                hash_con = b.get_hash_con()
                hash = b.get_hash().hexdigest()
                print("Time stamp in float: ", b.get_timestamp())
                print("Convergent Hash: ", hash_con)
                image = Image(name=image_path, image=filename,hash_con=hash_con, hash_div=hash_div, hash=hash, timestamp=b.get_timestamp())
                image.save()
                return Response(ImageSerializer(image).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        