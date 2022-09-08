from django.contrib import admin

##from .models import Guest, Hotel, Room, Booking
from .models import Room, Event, Customer


admin.site.register(Room)
admin.site.register(Event)
admin.site.register(Customer)

##admin.site.register(Guest)
##admin.site.register(Hotel)
##admin.site.register(Room)
##admin.site.register(Booking)

