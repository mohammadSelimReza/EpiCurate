from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserBioData, UserInfo


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True},
        }

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return data

    def create(self, validate_data):
        user = User(
            username=validate_data["username"],
            email=validate_data["email"],
            first_name=validate_data["first_name"],
            last_name=validate_data["last_name"],
        )
        user.set_password(validate_data["password"])
        user.is_active = False
        user.save()
        return user


class UserBioDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBioData
        fields = ["user_type", "user_position"]


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [
            "gender",
            "phone",
            "nid",
            "street_address",
            "city",
            "postal_code",
            "country",
        ]


class UserCreationSerializer(serializers.ModelSerializer):
    user = UserSerializers()
    user_bio_data = UserBioDataSerializer(
        source="*"
    )  # This flattens the nested serializer
    user_info = UserInfoSerializer(source="user.info")

    class Meta:
        model = UserBioData
        fields = ["user", "user_bio_data", "user_info"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        bio_data = {
            "user_type": validated_data.pop("user_type"),
            "user_position": validated_data.pop("user_position"),
        }
        info_data = validated_data.pop("user_info")

        # Create User instance
        user = UserSerializers().create(user_data)

        # Create UserBioData instance
        UserBioData.objects.create(user=user, **bio_data)

        # Create UserInfo instance
        UserInfo.objects.create(user=user, **info_data)

        return user
