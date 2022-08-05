from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegisterUserSerializer


class RegisterUser(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
