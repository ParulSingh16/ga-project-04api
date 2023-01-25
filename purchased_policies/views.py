from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# This provides a default response for a not found
from rest_framework.exceptions import NotFound

# this imports a Django core exception: ValidationError
from django.db import IntegrityError

from .models import PurchasedPolicy
from .serializers.populated import PurchasedPolicySerializer, PopulatedPurchasedPolicySerializer


class PurchasedPolicyListView(APIView):

    def get(self, _request):
        # get all of the partners from the database
        purchased_policies = PurchasedPolicy.objects.all()
        serialized_purchased_policies = PopulatedPurchasedPolicySerializer(
            purchased_policies, many=True)
        return Response(serialized_purchased_policies.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        request.data['owner']

        purchasedPolicy_to_add = PurchasedPolicySerializer(
            data=request.data)
        try:
            purchasedPolicy_to_add.is_valid()
            purchasedPolicy_to_add.save()
            return Response(purchasedPolicy_to_add.data, status=status.HTTP_201_CREATED)
        # exceptions are like a catch in js, but if we specify an exception like we do below then the exception thrown has to match to fall into it
        # For example the below is the exception thrown when we miss a required field
        # link: (this documentation entry is empty but shows it exists) https://docs.djangoproject.com/en/4.0/ref/exceptions/#django.db.IntegrityError
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            # IntegrityError is an exception thrown when fields are missing
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # AssertionError occurs when the incorrect type is passed as a value for an existing field
        # AssertionError is a native python error
        # link: https://docs.python.org/3/library/exceptions.html#AssertionError
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # If we leave it blank, (except:) then all exceptions will fall into it
        # We will add this as a fallback.
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class PurchasedPolicyDetailView(APIView):
    def get_policy(self, pk):
        try:
            return PurchasedPolicy.objects.get(pk=pk)
        except PurchasedPolicy.DoesNotExist:

            raise NotFound(detail="Can't find that policy!")

    def get(self, _request, pk):
        policy = self.get_policy(pk=pk)
        serialized_policy = PopulatedPurchasedPolicySerializer(policy)
        rate = (float(serialized_policy.data['insured_product_price']) * float(
            serialized_policy.data['policy']['increase_price']))
        data_with_calculated_rate = dict(serialized_policy.data)
        data_with_calculated_rate['rate'] = rate
        return Response(data_with_calculated_rate, status=status.HTTP_200_OK)
