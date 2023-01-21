from rest_framework import serializers
from ..models import Policy  # import the model


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy  # the model that our serializer should use to transform from the database
        fields = '__all__'  # specify which fields we want to return
