from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
from .models import Note, UserAccount
from .serializers import NoteSerializer


def createNote(request, user):
    data = request.data
    note = Note.objects.create(
        title=data['title'], tag=data['tag'], body=data['body'], user=user)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def getAllNotes(request, user):
    notes = Note.objects.filter(user=user).order_by('-updated_at')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


def getNote(request, pk, user):
    note = Note.objects.get(id=pk)
    if note.user != user:
        raise AuthenticationFailed(
            "This is not your note to get, nice try tho")
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def updateNote(request, pk, user):
    data = request.data
    note = Note.objects.get(id=pk)
    if note.user != user:
        raise AuthenticationFailed(
            "This is not your note to update, nice try tho")
    serializer = NoteSerializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


def deleteNote(request, pk, user):
    note = Note.objects.get(id=pk)
    if note.user != user:
        raise AuthenticationFailed(
            "This is not your note to delete, nice try tho")
    note.delete()
    return Response('Note was deleted!')


def getAuthenticatedUser(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed("Unauthenticated. Try logging in first!")
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated. Try logging in first!!")

    user = UserAccount.objects.filter(id=payload['id']).first()
    return user
