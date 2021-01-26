from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    first_name       = serializers.CharField(allow_blank=False , write_only=True)
    last_name        = serializers.CharField(allow_blank=False , write_only=True)
    confirm_password = serializers.CharField(allow_blank=False , write_only=False)


    class Meta:
        model = get_user_model()
        fields= ("phone_number", "first_name" , "last_name", "password","confirm_password", )


    def create(self, validated_data):
        # confirm_password = validated_data.pop("confirm_password")
        return get_user_model().objects.create_user(**validated_data)


    def validate(self, attrs):
        if not self.equal_password_confirm(attrs.get("password"),attrs.pop("confirm_password")):
            raise serializers.ValidationError ({"password": _("password and confirm_password is not equal")})
        return attrs


    def validated_password(self,password):
        if password.startwith("1234"):
            raise serializers.ValidationError(_("Password can't starts with 1234"))
        return password


    def equal_password_confirm (self,password=None,confirm_password=None):
        return True if password and confirm_password and password==confirm_password else False



