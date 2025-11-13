from django.forms import ModelForm,DateInput
from Airline.models  import Airport,Airline,Airplane,Flight,SeatClass,Passenger 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

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
        widgets = {
            'flight_date': DateInput(attrs={'type': 'date'}),
        }
        
class SeatForm(ModelForm):        
    class Meta:
        model = SeatClass
        fields = '__all__'
        
class PassengerForm(ModelForm):        
    class Meta:
        model = Passenger
        fields = '__all__'                        

class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Password'}))