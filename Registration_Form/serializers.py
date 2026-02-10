from rest_framework import serializers
from .models import Registration
import re
from datetime import date

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = '__all__'

    def validate_mobile_number(self, value):
        if not re.match(r'^[6-9]\d{9}$', value):
            raise serializers.ValidationError("Invalid mobile number")
        return value

    def validate_company_pan(self, value):
        if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', value):
            raise serializers.ValidationError("Invalid PAN format")
        return value.upper()

    def validate_company_gst(self, value):
        if not re.match(
            r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$',
            value
        ):
            raise serializers.ValidationError("Invalid GST number")
        return value.upper()

    def validate_establishment_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Year cannot be in future")
        return value

    def validate(self, data):
        if data['number_of_employees'] < 1:
            raise serializers.ValidationError(
                "Employees must be greater than zero"
            )
        return data