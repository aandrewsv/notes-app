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

    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.set_password(validated_data['password'])
        user.save()
        return user
