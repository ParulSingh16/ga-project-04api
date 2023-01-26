from .common import PurchasedPolicySerializer
from policies.serializers.populated import PopulatedPolicySerializer
from jwt_auth.serializers.common import UserSerializer


class PopulatedPurchasedPolicySerializer(PurchasedPolicySerializer):
    policy = PopulatedPolicySerializer()
    owner = UserSerializer()
