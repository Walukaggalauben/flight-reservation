from django.db import models

# Create your models here.

class Airport(models.Model):
    airport_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    #departure_airport = models.CharField(max_length=100)
    #arrival_airport = models.CharField(max_length=100)
    
class Airline(models.Model):
    airline_name = models.CharField(max_length=100)
    country =  models.CharField(max_length=100)
    hq_location = models.CharField(max_length=100)
    
class Airplane(models.Model):
    model = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    airline = models.ForeignKey(Airline,on_delete=models.CASCADE)
    
class Flight(models.Model):
    flight_date = models.DateField(auto_now=False)
    arrival_time = models.TimeField()
    departure_airport = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='departing_flights')
    arrival_airport = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='arriving_flights')
    departure_time = models.TimeField()
    airplane = models.ForeignKey(Airplane,on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline,on_delete=models.CASCADE)
    fare = models.IntegerField(default=0)
    currency = models.CharField(max_length=100)
    
class SeatClass(models.Model):
    plane = models.ForeignKey(Airplane,on_delete=models.CASCADE)
    capacity = models.IntegerField(default=0)
                          
    
class Passenger(models.Model):
    GENDER_OPTION=[
        ("F","Female"),
        ("M","Male")
    ]
    passenger_first_name = models.CharField(max_length=100)
    passenger_last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=8,choices=GENDER_OPTION)
    address = models.CharField(max_length=100,null=True,blank=True,default="N/A")
    contact = models.CharField(max_length=10)
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passport_no = models.CharField(max_length=100)
    seatclass = models.ForeignKey(SeatClass,on_delete=models.CASCADE)
                  
