from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class HelloApiView(APIView):
    '''TEST API View'''
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        '''Return a list of APIView features'''
        an_apiview = [
            'Uses HTTP method as function (get, poast, path, put, delete)',
            'Is silimal to a traditional Django View',
            'Gives you the most contrtol over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        '''Create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message': message})

        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''Handle updating an object'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''Handle a partial update of an object'''
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        '''Delete an object'''
        return Response({'method': 'DELETE'})