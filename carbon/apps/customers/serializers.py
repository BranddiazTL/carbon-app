from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "user",
            "image",
            "home_address",
            "work_address",
            "city",
            "status",
        ]
