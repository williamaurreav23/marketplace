from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.utils.translation import ugettext_lazy as _

from marketplace.supporters.models import Supporter, Alert
from marketplace.athletes.api.v1.serializers import AthleteSerializer
from marketplace.users.models import User
from marketplace.athletes.models import Athlete


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('rule', 'amount', 'supporter', 'athlete')


class SupporterSerializer(serializers.ModelSerializer):
    alerts = AlertSerializer(many=True, read_only=True)
    followers = AthleteSerializer(many=True, read_only=True)

    class Meta:
        model = Supporter
        fields = ('alerts', 'followers')


class SupporterRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(),
                                                               message=_('There is another user with this email'))])
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    repeat_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate_password(self, value):
        password_validation.validate_password(password=value, user=User)
        return value

    def validate(self, data):
        if data['password'] != data['repeat_password']:
            raise serializers.ValidationError("Password does not match the confirm password.")
        return data