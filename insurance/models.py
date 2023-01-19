from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=50)
    emailId = models.CharField(primary_key=True, max_length=300)
    password = models.CharField(max_length=10)
    signupDate = models.DateField

    # this function represents the class objects as a string in the admin app


class Partner(models.Model):
    pName = models.CharField(max_length=50)
    pCode = models.CharField(primary_key=True, max_length=5)
    onboardingDate = models.DateField


class Rate(models.Model):
    pCode = models.CharField(max_length=5)
    productRate = models.IntegerField
    insuranceRate = models.IntegerField


class Policy(models.Model):
    policyId = models.CharField(primary_key=True, max_length=20)
    customerId = models.CharField(max_length=300)
    pCode = models.CharField(max_length=5)
    productName = models.CharField(max_length=100)
    productRate = models.IntegerField
    insuranceRate = models.IntegerField
    policyDate = models.DateField
    isClaimed = models.BooleanField(blank=False)
    claimDate = models.DateField
    claimReason = models.CharField(max_length=10)
