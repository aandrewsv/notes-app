from rest_framework.serializers import ModelSerializer
from .models import Note, User


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
