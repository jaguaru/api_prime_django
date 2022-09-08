####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

##from django.db import models
from datetime import timedelta, datetime
from django.db import models
from datetime import datetime


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
class Room(models.Model):

      room_id = models.AutoField(primary_key=True)
      room_code = models.CharField(max_length=8)
      name = models.CharField(max_length=4)
      capacity = models.IntegerField(default=7)
      status = models.BooleanField(default=False)
      created = models.DateField()
      updated = models.DateField()

      def __str__(self) -> str:
          return self.room_code


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
class Event(models.Model):

      event_id = models.AutoField(primary_key=True)
      event_code = models.CharField(max_length=8)
      name = models.CharField(max_length=32)
      event_type = models.CharField(max_length=8)
      status = models.BooleanField(default=False)
      fk_room_code = models.CharField(max_length=8)
      fk_customer_code = models.CharField(max_length=8)
      created = models.DateField()
      updated = models.DateField()

      def __str__(self) -> str:
          return self.event_code


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
class Customer(models.Model):

      customer_id = models.AutoField(primary_key=True)
      customer_code = models.CharField(max_length=8)
      phone = models.CharField(max_length=12)
      name = models.CharField(max_length=32)
      lastname = models.CharField(max_length=32)
      status = models.BooleanField(default=False)
      created = models.DateField()
      updated = models.DateField()

      def __str__(self) -> str():
          return self.customer_code


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

# ####--------------------------------------------------------------------------------------------------------------
# ####--------------------------------------------------------------------------------------------------------------
# class Guest(models.Model):
    
#     name  = models.CharField(max_length=20)
#     age   = models.IntegerField(default=20)
#     phone = models.CharField(max_length=20)
#     email = models.CharField(max_length=30)

#     def __str__(self) -> str:
#         return self.name


# ####--------------------------------------------------------------------------------------------------------------
# ####--------------------------------------------------------------------------------------------------------------
# class Hotel(models.Model):
    
#     name     = models.CharField(max_length=20)
#     location = models.CharField(max_length=50)
#     phone    = models.CharField(max_length=20)
#     email    = models.CharField(max_length=30)

#     def __str__(self) -> str:
#         return self.name


# ####--------------------------------------------------------------------------------------------------------------
# ####--------------------------------------------------------------------------------------------------------------
# class Room(models.Model):
    
#     room_no   = models.IntegerField(default=101)
#     price     = models.FloatField(default=1000.0)
#     hotel     = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     is_booked = models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return str(self.room_no)

#     def hotel_name(self) -> str:
#         return self.hotel


# ####--------------------------------------------------------------------------------------------------------------
# ####--------------------------------------------------------------------------------------------------------------
# class Booking(models.Model):
    
#     guest         = models.ForeignKey(Guest, on_delete=models.CASCADE)
#     hotel         = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     room          = models.ForeignKey(Room, on_delete=models.CASCADE)
#     num_of_guest  = models.IntegerField(default=1)
#     checkin_date  = models.DateField(default=datetime.now)
#     checkout_date = models.DateField(default=datetime.now)
#     is_checkout   = models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return self.guest.name

#     def hotel_name(self) -> str:
#         return self.hotel.hotel

#     def charge(self) -> float:
#         return self.is_checkout*(self.checkout_date - self.checkin_date + timedelta(1)).days*self.room.price


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

