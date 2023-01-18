from rest_framework import serializers
from authentication.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'nickname', 'photo', 'description', 'is_active', 'password']
        extra_kwargs = {
            'password'   : {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    
    def validate_password(self, value):
        for i in range(len(value)-2):
            search_value = value[i:i+3]
            if self.initial_data['email'].find(search_value) != -1:
                raise serializers.ValidationError("Passwrod is too similar to your email. Please try another one.")
        
        if len(value) < 8:
            raise serializers.ValidationError("Passwrod has to be not shorter than 8 characters")
        
        return value
