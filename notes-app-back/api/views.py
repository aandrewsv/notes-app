from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import createNote, deleteNote, getAllNotes, updateNote, getNote, getAuthenticatedUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


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


@api_view(['GET', 'POST'])
def getNotes(request):
    permission_classes = (IsAuthenticated)

    if request.method == 'GET':
        return getAllNotes(request, request.user)

    if request.method == 'POST':
        return createNote(request, request.user)


@api_view(['GET', 'PUT', 'DELETE'])
def handleNote(request, pk):
    permission_classes = (IsAuthenticated)
    if request.method == 'GET':
        return getNote(request, pk, request.user)

    if request.method == 'PUT':
        return updateNote(request, pk, request.user)

    if request.method == 'DELETE':
        return deleteNote(request, pk, request.user)
