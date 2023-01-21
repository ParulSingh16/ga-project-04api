from .common import PolicySerializer
from partners.serializers.common import PartnerSerializer


class PopulatedPolicySerializer(PolicySerializer):
    provider = PartnerSerializer()
