from django.db import models
from django.core.validators import RegexValidator

#CRUD
#C-CREATE
#R-READ
#U-UPDATE
#D-DELETE 

# Create your models here.

class Airport(models.Model):
    airport_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    #departure_airport = models.CharField(max_length=100)
    #arrival_airport = models.CharField(max_length=100)
    
    def __str__(self):
        return self.airport_name
    
class Airline(models.Model):
    airline_name = models.CharField(max_length=100)
    country =  models.CharField(max_length=100)
    hq_location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.airline_name
    
class Airplane(models.Model):
    model = models.CharField(max_length=100)
    capacity = models.IntegerField(max_length=100)
    airline = models.ForeignKey(Airline,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.model
    
class Flight(models.Model):
    flight_date = models.DateField(auto_now=False)
    departure_time = models.TimeField()
    departure_airport = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='departure_airport')
    arrival_airport = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='arrival_airport')
    arrival_time = models.TimeField()
    airplane = models.ForeignKey(Airplane,on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline,on_delete=models.CASCADE)
    fare = models.IntegerField(default=0)
    currency = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.departure_airport} to {self.arrival_airport} on {self.flight_date}" 
       #return f"{self.airline} Flight from {self.departure_airport} to {self.arrival_airport} on {self.flight_date}"
        
    
class SeatClass(models.Model):
    CLASS_CHOICE = [
        ("ECONOMY","Economy class"),
        ("BUSINESS","Business class"),
        ("FIRST","First Class")
    ]
    seat_type = models.CharField(max_length=50,choices=CLASS_CHOICE)
    plane = models.ForeignKey(Airplane,on_delete=models.CASCADE)
    capacity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.seat_type
                          
    
class Passenger(models.Model):
    GENDER_OPTION=[
        ("F","Female"),
        ("M","Male")
    ]
    #SEAT_CLASS_OPTION=[
     #  ("E","Economy"),
      # ("B","Business"),
       #("F","First Class")
    #]
    ROLES = [
        ("ADMIN","Admin"),
        ("PASSENGER","Passenger")
    ]
    role = models.CharField(max_length=10,choices=ROLES,default="ADMIN")
    passenger_first_name = models.CharField(max_length=100)
    passenger_last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=8,choices=GENDER_OPTION)
    address = models.CharField(max_length=100,null=True,blank=True,default="N/A")
    contact = models.CharField(max_length=10,validators=[RegexValidator(regex=r'^\d{10}$', message='Enter a valid 10-digit phone number')])
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passport_no = models.CharField(max_length=100)
    seatclass = models.ForeignKey(SeatClass,on_delete=models.CASCADE)#,choices=SEAT_CLASS_OPTION)
    
    def __str__(self):
        return f"{self.passenger_first_name} {self.passenger_last_name}"
                  
