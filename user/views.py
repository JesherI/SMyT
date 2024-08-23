from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import serializers
from user.models import Student

from rest_framework import serializers
from user.models import Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'email', 'curp', 'password')

    def create(self, validated_data):
        # Asegúrate de manejar la creación del usuario correctamente
        user = Student(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            curp=validated_data.get('curp'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user



@api_view(['POST'])
def login(request):
    user = get_object_or_404(Student, username=request.data.get('username'))
    if not user.check_password(request.data.get('password')):
        return Response({"error": "invalid password"}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = Student.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        Token.objects.create(user=user)
        return Response({'token': Token.objects.get(user=user).key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    print(request.user)
    return Response("You are login  wit {}".format(request.user.username), status=status.HTTP_200_OK)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({'detail': 'Successfully logged out'}, status=status.HTTP_200_OK)
    except Token.DoesNotExist:
        return Response({'error': 'Token does not exist'}, status=status.HTTP_400_BAD_REQUEST)