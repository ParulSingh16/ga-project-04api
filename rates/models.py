from django.db import models


class Rate(models.Model):
    partner = models.ForeignKey(
        'partners.Partner', related_name="partner", on_delete=models.CASCADE)
    productRate = models.IntegerField()
    insuranceRate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.pCode} - {self.productRate} - {self.insuranceRate}"
