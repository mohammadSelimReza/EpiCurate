from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserInfo


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
        ]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserCreationSerializer(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = UserInfo
        fields = [
            "user",
            "id",
            "user_type",
            "user_position",
            "gender",
            "phone",
            "nid",
            "street_address",
            "city",
            "postal_code",
            "country",
            "salary",
            "is_owner",
            "is_manager",
            "is_worker",
            "is_customer",
        ]

    def create(self, validated_data):
        # Extract user data and create a User instance
        user_data = validated_data.pop("user")
        user = UserSerializers.create(UserSerializers(), validated_data=user_data)

        # Create a UserInfo instance with the remaining fields
        user_info = UserInfo.objects.create(
            user=user,
            id=validated_data.get("id"),
            user_type=validated_data.get("user_type"),
            user_position=validated_data.get("user_position"),
            gender=validated_data.get("gender"),
            phone=validated_data.get("phone"),
            nid=validated_data.get("nid"),
            street_address=validated_data.get("street_address"),
            city=validated_data.get("city"),
            postal_code=validated_data.get("postal_code"),
            country=validated_data.get("country"),
            salary=validated_data.get("salary", 0),
            is_owner=validated_data.get("is_owner", False),
            is_manager=validated_data.get("is_manager", False),
            is_worker=validated_data.get("is_worker", False),
            is_customer=validated_data.get("is_customer", False),
        )

        return user_info
