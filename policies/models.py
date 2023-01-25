from django.db import models


class Policy(models.Model):
    name = models.CharField(max_length=50)
    increase_price = models.DecimalField(decimal_places=2, max_digits=4)
    provider = models.ForeignKey(
        'partners.Partner', related_name='policies', on_delete=models.CASCADE, db_column="provider_id")

    def __str__(self):
        return f"{self.name}"
