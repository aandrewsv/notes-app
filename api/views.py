from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .utils import createNote, deleteNote, getAllNotes, updateNote, getNote
from .serializers import UserSerializer


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

# @api_view(['POST'])
# def signIn(request):
#     pass


@api_view(['GET', 'POST'])
def getNotes(request):
    if request.method == 'GET':
        return getAllNotes(request)

    if request.method == 'POST':
        return createNote(request)


@api_view(['GET', 'PUT', 'DELETE'])
def handleNote(request, pk):
    if request.method == 'GET':
        return getNote(request, pk)

    if request.method == 'PUT':
        return updateNote(request, pk)

    if request.method == 'DELETE':
        return deleteNote(request, pk)
