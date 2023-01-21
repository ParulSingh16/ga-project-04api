from rest_framework import serializers
from ..models import PurchasedPolicy  # import the model


class PurchasedPolicySerializer(serializers.ModelSerializer):
    class Meta:
        # the model that our serializer should use to transform from the database
        model = PurchasedPolicy
        fields = '__all__'  # specify which fields we want to return
