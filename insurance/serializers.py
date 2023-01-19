from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer  # the model that our serializer should use to transform from the database
        fields = '__all__'  # specify which fields we want to return
