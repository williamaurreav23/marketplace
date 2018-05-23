from rest_framework import serializers
from marketplace.athletes.models import Picture, Link, Athlete
from marketplace.users.models import User


class PictureSerializer(ModelSerializer):
    class Meta:
        model = Picture
        fields = ('image',)


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ('name', 'url',)


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ('id', 'first_name', 'last_name', 'country', 'sex', 'date_of_birthday',
                  'sport', 'state')


class AthleteRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    country = serializers.CharField()
    sex = serializers.CharField()
    date_of_birthday = serializers.DateField()
    sport = serializers.CharField()
    state = serializers.CharField()
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(),
                                                               message=_('There is another user with this email'))])
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    repeat_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate_password(self, data):
        password_validation.validate_password(password=data, user=User)
        return data

    def validate(self, data):
        if data['password'] != data['repeat_password']:
            raise serializers.ValidationError("Password does not match the confirm password.")
        return data

