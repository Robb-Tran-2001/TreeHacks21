from rest_framework import serializers
from .models import User, Image
from versatileimagefield.serializers import VersatileImageFieldSerializer
#convert python object to json for each type of HttpRequest
#keeps track of necessary parameters in payload
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

#for login and signup
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"

class CreateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"