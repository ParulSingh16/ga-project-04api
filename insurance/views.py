from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Customer
from .serializers import CustomerSerializer, PopulatedCustomerSerializer
from django.shortcuts import render
from .models import StudentDetails


class CustomerRegisteration(APIView):
    # This sets the permission levels of specific views by passing the framework authentication class.
    permission_classes = (IsAuthenticatedOrReadOnly,)

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
