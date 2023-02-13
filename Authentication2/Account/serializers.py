from rest_framework import serializers
from Account.models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields="__all__"

    def validate(self, attrs):
        password=attrs.get('password')
        user_id=attrs.get('user_id')
        username =attrs.get('username')
        checkdata=CustomUser.objects.filter(username=username,user_id=user_id).last()
        print(checkdata)

        if checkdata:
            raise serializers.ValidationError("User already exists")
            return attrs
        else:
            cust=CustomUser.objects.create(user_id=user_id,password=password,is_superuser=False,first_name="kamal",last_name="kant",username=username,email="kk@gmail.com",is_staff=False,is_active=True,)
            return cust
    # def create(self, validated_data):

    #     return CustomUser.objects.create(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields="__all__"