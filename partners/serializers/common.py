from rest_framework import serializers
from ..models import Partner  # import the model


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner  # the model that our serializer should use to transform from the database
        fields = '__all__'  # specify which fields we want to return
