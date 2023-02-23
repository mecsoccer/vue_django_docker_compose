from rest_framework import serializers
from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ["id", "email", "first_name", "last_name", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserInfo.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user