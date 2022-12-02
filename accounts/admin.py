from django.contrib import admin

from .models import Adminstrator, Customer

# Register your models here.
admin.site.register(Adminstrator)
admin.site.register(Customer)
