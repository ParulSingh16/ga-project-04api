from django.contrib import admin
from .models import Customer
from .models import Partner
from .models import Rate
from .models import Policy


# Register your models here.
admin.site.register(Customer)
admin.site.register(Partner)
admin.site.register(Rate)
admin.site.register(Policy)
