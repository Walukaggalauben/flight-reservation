from django.contrib import admin
from.models import Airport,Airline,Airplane,Flight,Passenger,SeatClass

# Register your models here.



class AirportAdmin(admin.ModelAdmin):
    list_display=("airport_name","country","city")
class AirlineAdmin(admin.ModelAdmin):
    list_display=("airline_name","country","hq_location")
class AirplaneAdmin(admin.ModelAdmin):
    list_display=("model","capacity","airline")
class FlightAdmin(admin.ModelAdmin):
    list_display=("flight_date","departure_time","departure_airport","arrival_airport","arrival_time","airplane","airline","fare","currency")
class SeatClassAdmin(admin.ModelAdmin):
    list_display=("seat_type","plane","capacity") 
class PassengerAdmin(admin.ModelAdmin):
    list_display=("passenger_first_name","passenger_last_name","gender","address","contact","flight","passport_no","seatclass")
                  

admin.site.register(Airport,AirportAdmin)
admin.site.register(Airline,AirlineAdmin)
admin.site.register(Airplane,AirplaneAdmin)
admin.site.register(Flight,FlightAdmin)
admin.site.register(Passenger,PassengerAdmin)
admin.site.register(SeatClass,SeatClassAdmin)    