from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from wheel.metadata import _

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("id",)

    def validate(self, attrs):
        password1 = attrs.get("password1")
        password2 = attrs.pop("password2", None)
        username = attrs.get("username")
        user = User.objects.filter(username=username).exists() if username else None
        if user:
            raise ValidationError(_('Username is already taken.'))
        if password2 != password1:
            raise ValidationError(_("Passwords didn't match."))
        return super().validate(attrs)

    def create(self, validated_data):
        password1 = validated_data.pop("password1", None)
        user = User(**validated_data)
        user.set_password(password1)
        user.save()
        return user
