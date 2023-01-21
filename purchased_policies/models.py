from django.db import models


class PurchasedPolicy(models.Model):
    policy = models.ForeignKey(
        'policies.Policy', related_name='policy_name', on_delete=models.CASCADE)
    owner = models.ForeignKey(
        'jwt_auth.User', related_name="owner", on_delete=models.CASCADE)
    insured_product = models.CharField(max_length=100)
    insured_product_price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.insured_product}"
