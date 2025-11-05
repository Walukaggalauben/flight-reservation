#we started by creating our form,method to create a form is to use ModelForm then views if it is valid we save if a get then we just display create an empty form
#Then we pass the form to our context wc is a dictionary containing all values or data to forward to the template 
#load template then pass context along with it 


from django.forms import ModelForm
from Airline.models  import Airport,Airline,Airplane,Flight,SeatClass,Passenger 

class AirportForm(ModelForm):
    class Meta:
        model = Airport
        fields = '__all__' #{"airport_name","country","city"}#matching names with in models.py

class AirlineForm(ModelForm):        
    class Meta:
        model = Airline
        fields = '__all__'

class AirplaneForm(ModelForm):        
    class Meta:
        model = Airplane
        fields = '__all__'
        
class FlightForm(ModelForm):        
    class Meta:
        model = Flight
        fields = '__all__'
        
class SeatForm(ModelForm):        
    class Meta:
        model = SeatClass
        fields = '__all__'
        
class PassengerForm(ModelForm):        
    class Meta:
        model = Passenger
        fields = '__all__'                        