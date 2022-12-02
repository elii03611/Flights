from django.contrib import admin

from .models import Airline_Companie, Countrie, Flight, Ticket

# Register your models here.
admin.site.register(Countrie)
admin.site.register(Airline_Companie)
admin.site.register(Flight)
admin.site.register(Ticket)



