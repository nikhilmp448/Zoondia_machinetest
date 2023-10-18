from rest_framework import serializers
from user.models import Account
import re

class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only = True, required = True , style = {'input_type': 'password'})
    confirm_password = serializers.CharField(write_only = True, required = True , style = {'input_type': 'confirm_password'})

    def validate_password(self,value):
        if len(value) <8 :
            raise serializers.ValidationError("password must contain atleast 8 chara")
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("password must contain atleast one uppercase")
        if not re.search(r'[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]',value):
            raise serializers.ValidationError("password must contain atleast one special chara")
        
        return value
    
    def validate(self,data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password !=confirm_password:
            raise serializers.ValidationError("password not matching")
        
        return data

    class Meta:
        
        model = Account
        fields = ('email','password','firstName','lastName')

        def create(self,validated_data):

            user = Account(
                email = validated_data['email'],
                firstname = validated_data['firstName'],
                lastName = validated_data['lastName']            

            )
            password  = self.validate_password(validated_data['password'])
            user.set_password(password)
            user.save()
            return user
    