from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view


from .models import Customer
from .serializers import CustomerSerializer
from django.shortcuts import render


class CustomerRegisteration(APIView):
    # This sets the permission levels of specific views by passing the framework authentication class.
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    # Create your views here.

    def indexpage(req):
        return render(req, 'index.html')

    def newPage(request):
        emailId = request.POST.get("emailId")
        userName = request.POST.get("userName")
        password = request.POST.getlist("password")

        o_ref = Customer(emailId=emailId,  userName=userName,
                         password=password)
        o_ref.save()

        # the resgisteration form that will be created in mongo db will be called here.
        return render(request, 'index.html', {"message": "registered!"})

    @api_view(['POST'])
    def add_items(request):
        item = CustomerSerializer(data=request.data)

    # validating for already existing data
        if Customer.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')

        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET'])
    def view_items(request):

        # checking for the parameters from the URL
        items = Customer.objects.all()
        serializer = CustomerSerializer(items, many=True)

    # if there is something in items else raise error
        if items:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


# the below was used before and didnt get the api then was replaced by the above code

#             @api_view(['GET'])
# def view_items(request):

#     # checking for the parameters from the URL
#     if request.query_params:
#         items = Item.objects.filter(**request.query_param.dict())
#     else:
#         items = Item.objects.all()

#     # if there is something in items else raise error
#     if items:
#         data = ItemSerializer(items)
#         return Response(data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
