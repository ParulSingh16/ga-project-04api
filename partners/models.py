from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    onboarding_date = models.DateField()

    def __str__(self):
        return f"{self.name}"
