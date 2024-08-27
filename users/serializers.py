from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'full_name', 'artistic_name']
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {
                'validators': [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            'email': {
                'validators': [
                    UniqueValidator(queryset=User.objects.all())
                ]
            },
            'password': {'write_only': True},
            'full_name': {'required': False},
        }


    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
    

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        if password:
            instance.set_password(password)

        instance.save()

        return instance
