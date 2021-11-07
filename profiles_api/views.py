from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''TEST API View'''


    def get(self, request, format=None):
        '''Return a list of APIView features'''
        an_apiview = [
            'Uses HTTP method as function (get, poast, path, put, delete)',
            'Is silimal to a traditional Django View',
            'Gives you the most contrtol over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})