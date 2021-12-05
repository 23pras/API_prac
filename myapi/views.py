from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.http import Http404
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView




# Create your views here.
@api_view()
def detail(request, userid):
    try:
        person = Person.objects.get(userId=userid)
        serializer=PersonSerializer(person)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return Response(serializer.data)


@api_view()
def personALL(request):
    try:
        person = Person.objects.all()
        serializer=PersonSerializer(person, many=True)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return Response(serializer.data)



# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})
import json

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        print(request.data)
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})



class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.FirstName for user in Person.objects.all()]
        return Response(usernames)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



































































