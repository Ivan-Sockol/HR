from rest_framework import serializers
from .models import Resume, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
        read_only_fields = ['id']

class ResumeSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='user.username')
    owner_role = serializers.ReadOnlyField(source='user.get_role_display')
    class Meta:
        model = Resume
        fields = [
            'id', 'user', 'owner_name', 'owner_role',
            'created_at', 'experience',
        ]
        read_only_fields = ("user", 'created_at')

    def create(self, validated_data):
        validated_data['data'] = self.context['request'].user
        return super().create(validated_data)