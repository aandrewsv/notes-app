from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
import jwt
from api.models import User
from .utils import createNote, deleteNote, getAllNotes, updateNote, getNote, getAuthenticatedUser
from .serializers import UserSerializer
import datetime

from api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/',
            'method': 'POST',
            'body': {'title': "", 'body': "", 'tag': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },

        {
            'Endpoint': '/notes/id/',
            'method': 'PUT',
            'body': {'title': "", 'body': "", 'tag': ""},
            'description': 'Updates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view(['POST'])
@permission_classes([AllowAny])
def signUp(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response('¡User successfully created!')


@api_view(['POST'])
@permission_classes([AllowAny])
def signIn(request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(email=email).first()
    if user is None:
        raise AuthenticationFailed("The email provided isn't registered")

    if not user.check_password(password):
        raise AuthenticationFailed('Password is Incorrect!')

    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['GET'])
@permission_classes([AllowAny])
def userView(request):
    user = getAuthenticatedUser(request)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def signOut(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        "detail": "success"
    }
    return response


@api_view(['GET', 'POST'])
def getNotes(request):
    user = getAuthenticatedUser(request)
    if request.method == 'GET':
        return getAllNotes(request, user)

    if request.method == 'POST':
        return createNote(request, user)


@api_view(['GET', 'PUT', 'DELETE'])
def handleNote(request, pk):
    user = getAuthenticatedUser(request)
    if request.method == 'GET':
        return getNote(request, pk, user)

    if request.method == 'PUT':
        return updateNote(request, pk, user)

    if request.method == 'DELETE':
        return deleteNote(request, pk, user)
