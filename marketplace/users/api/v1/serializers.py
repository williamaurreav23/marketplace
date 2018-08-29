from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from marketplace.athletes.api.v1.serializers import AthleteSerializer
from marketplace.supporters.api.v1.serializers import SupporterSerializer
from marketplace.users.models import User


class UserSerializer(serializers.ModelSerializer):
    athlete = AthleteSerializer(read_only=True)
    supporter = SupporterSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'athlete', 'supporter', 'is_staff')


class RequestRestoreCodeSerializer(serializers.Serializer):
    """Serializer to request a new password for the user."""

    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("Email not found"))
        return value

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class RestorePasswordSerializer(serializers.Serializer):
    """Serializer to restore a password for the user."""

    password = serializers.CharField()
    repeat_password = serializers.CharField()
    restore_password_code = serializers.CharField()

    def validate_restore_password_code(self, value):
        if not User.objects.filter(restore_password_code=value).exists():
            raise serializers.ValidationError(_("Restore code doesn't exists"))
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        repeat_password = attrs.get('repeat_password')
        if password and repeat_password and password != repeat_password:
            raise serializers.ValidationError(_("Passwords are not the same"))
        return attrs

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class VerifySerializer(serializers.Serializer):
    """Serializer to verify the user's email."""

    verification_code = serializers.CharField()

    def validate_verification_code(self, value):
        if not User.objects.filter(verification_code=value).exists():
            raise serializers.ValidationError(_("Verification code not found"))
        return value

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
