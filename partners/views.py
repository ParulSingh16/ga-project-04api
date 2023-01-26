from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# This provides a default response for a not found
# from rest_framework.exceptions import NotFound
# this imports a Django core exception: ValidationError
from django.db import IntegrityError
from .models import Partner
from .serializers.common import PartnerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PartnerListView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly, )#not needed authentication for partners

    def get(self, _request):
        partners = Partner.objects.all()  # get all of the partners from the database
        serialized_partners = PartnerSerializer(partners, many=True)
        return Response(serialized_partners.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['owner'] = request.user.id
        partner_to_add = PartnerSerializer(data=request.data)
        print(partner_to_add)
        try:
            partner_to_add.is_valid()
            partner_to_add.save()
            return Response(partner_to_add.data, status=status.HTTP_201_CREATED)
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
        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
