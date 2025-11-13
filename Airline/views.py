from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from Airline.forms import AirportForm
from Airline.models import Airport

from Airline.forms import AirlineForm
from Airline.models import Airline

from Airline.forms import AirplaneForm
from Airline.models import Airplane

from Airline.forms import FlightForm    
from Airline.models import Flight

from Airline.forms import PassengerForm
from Airline.models import Passenger

from Airline.forms import SeatForm
from Airline.models import SeatClass
from Airline.forms import LoginForm
from django.contrib.auth import login, logout

# Create your views here.



    

def home_view(request):
    return render(request,'home.html')

@login_required
def airline_view(request):
    message = ''
    if request.method == "POST":
        airline_form = AirlineForm(request.POST)
        if airline_form.is_valid():
            airline_form.save()
            message = "Airline Added Successfully"
    else:        
        airline_form = AirlineForm()

    airlines = Airline.objects.all()    

    context = {
        'form': airline_form,
        'message': message,
        'airlines': airlines
    }
    return render(request,'airline.html',context)

    
@login_required
def delete_airline(request,airline_id):
    airline = Airline.objects.get(id = airline_id)
    if airline:
        print('Airline got')
        airline.delete()
       
        return redirect('airline_page')

    else:
        print('Airline not found')
        message = 'Airline Not Found'
        return render(request,'airline.html')

@login_required    
def edit_airline(request,airline_id):
    airline =  Airline.objects.get(id = airline_id)
    if request.method == 'POST':
        if airline:
            airline_form = AirlineForm(request.POST,instance=airline)
            if airline_form.is_valid():
                airline_form.save()
                return redirect('airline_page')


    else:        
        airline_form = AirlineForm(instance=airline)
        
        airlines = Airline.objects.all()
        
        context = {
            'form': airline_form,
            'airlines': airlines
        }        
        return render(request,'edit_passenger.html',context)    

# @login_required
def airplane_view(request):
    message = ''
    if request.method == "POST":
        airplane_form = AirplaneForm(request.POST)
        if airplane_form.is_valid():
            airplane_form.save()
            message = "Airplane Added Successfully"
   
    if request.method == "DELETE":
        airplane_id = request.POST.get('airplane_id')
        airplane = Airplane.objects.get(id=airplane_id)
        airplane.delete()
        message = "Airplane Deleted Successfully"
   
   
    else:        
        airplane_form = AirplaneForm()
        
    airplanes = Airplane.objects.all()
    
    context = {
        'form': airplane_form,
        'message': message,
        'airplanes': airplanes
    }        
    return render(request,'airplane.html',context)

@login_required
def airport_view(request):
    message = ""
    if request.method == "POST":
        airport_form = AirportForm(request.POST)
        if airport_form.is_valid():
            airport_form.save()
            message = "Airport Added Successfully"
    else:
        airport_form = AirportForm()

    airports = Airport.objects.all()  

    context = {
        'form': airport_form,  
        'message': message,
        'airports': airports
    }
    return render(request,'airport.html',context)

@login_required
def delete_airport(request,airport_id):
    airport = Airport.objects.get(id = airport_id)
    if airport:
        print('Airport got')
        airport.delete()
       
        return redirect('airport_page')

    else:
        print('Airport not found')
        message = 'Airport Not Found'
        return render(request,'airport.html')

@login_required    
def edit_airport(request,airport_id):
    airport =  Airport.objects.get(id = airport_id)
    if request.method == 'POST':
        if airport:
            airport_form = AirportForm(request.POST,instance=airport)
            if airport_form.is_valid():
                airport_form.save()
                return redirect('airport_page')


    else:        
        airport_form = AirportForm(instance=airport)
        
        airports = Airport.objects.all()
        
        context = {
            'form': airport_form,
            'airports': airports
        }        
        return render(request,'edit_passenger.html',context)    

@login_required
def flight_view(request):
    message = ''
    
    if request.method == "POST":
        flight_form = FlightForm(request.POST)
        if flight_form.is_valid():
            flight_form.save()
            message = "Flight Added Successfully"
    else:
        flight_form = FlightForm()
        
    flights = Flight.objects.all()
    
    context = {
        'form': flight_form,
        'message': message,
        'flights': flights
    }
    return render(request,'flight.html',context)

@login_required
def delete_flight(request,flight_id):
    flight = Flight.objects.get(id = flight_id)
    if flight:
        print('Flight got')
        flight.delete()
       
        return redirect('flight_page')

    else:
        print('Flight not found')
        message = 'Flight Not Found'
        return render(request,'flight.html')


@login_required
def edit_flight(request,flight_id):
    flight =  Flight.objects.get(id = flight_id)
    if request.method == 'POST':
        if flight:
            flight_form = FlightForm(request.POST,instance=flight)
            if flight_form.is_valid():
                flight_form.save()
                return redirect('flight_page')


    else:        
        flight_form = FlightForm(instance=flight)
        
        flights = Flight.objects.all()
        
        context = {
            'form': flight_form,
            'flights': flights
        }        
        return render(request,'edit_passenger.html',context)


@login_required
def passenger_view(request):
    message = ''
    if request.method == "POST":
        passenger_form = PassengerForm(request.POST)
        if passenger_form.is_valid():
            passenger_form.save()
            message = "Passenger Added Successfully"
    else:        
        passenger_form = PassengerForm()
    passengers = Passenger.objects.all()
    
    context = {
        'form': passenger_form,
        'message': message,
        'passengers': passengers
    }
    return render(request,'passenger.html',context)

@login_required
def delete_passenger(request,passenger_id):
    passenger = Passenger.objects.get(id=passenger_id)
    passenger.delete()
    return redirect('passenger_page')
    
def edit_passenger(request,passenger_id):
    passenger = Passenger.objects.get(id=passenger_id)
    if request.method == 'POST':
        passenger_form = PassengerForm(request.POST, instance=passenger)
        if passenger_form.is_valid():
            passenger_form.save()
            return redirect('passenger_page')
    else:
        passenger_form = PassengerForm(instance=passenger)

    passengers = Passenger.objects.all()
    context = {
        'form': passenger_form,
        'passengers': passengers,
        'passenger': passenger,
    }
    return render(request, 'edit_passenger.html', context)

@login_required
def seat_view(request):
    message = ''
    if request.method == "POST":
        seat_form = SeatForm(request.POST)
        if seat_form.is_valid():
            seat_form.save()
            message = "SeatClass Added Successfully"
    else:        
        seat_form = SeatForm()
    seat_class = SeatClass.objects.all()
        
    context = {
        'form': seat_form,
        'message': message,
        'seat_class': seat_class,
    }
    return render(request,'seat_class.html',context)

def delete_seat_class(request,seat_class_id):
    seat_class = SeatClass.objects.get(id = seat_class_id)
    seat_class.delete()
    
    return redirect('seat_page')

@login_required
def edit_seat_class(request,seat_class_id):
    seat_class =  SeatClass.objects.get(id = seat_class_id)
    if request.method == 'POST':
        if seat_class:
            seat_form = SeatForm(request.POST,instance=seat_class)
            if seat_form.is_valid():
                seat_form.save()
                return redirect('seat_page')


    else:        
        seat_form = SeatForm(instance=seat_class)
        
        seats = SeatClass.objects.all()
        
        context = {
            'form': seat_form,
            'seats': seats
        }        
        return render(request,'edit_passenger.html',context)


def Passenger_home_view(request):
    return render(request,'passenger_home.html')

@login_required
def deleteairplane(request,airplane_id):
    airplane = Airplane.objects.get(id = airplane_id)
    if airplane:
        print('Airplane got')
        airplane.delete()
       
        return redirect('airplane_page')

    else:
        print('Airplane not found')
        message = 'Airplane Not Found'
        return render(request,'airplane.html')

@login_required
def edit_airplane(request,airplane_id):
    plane =  Airplane.objects.get(id = airplane_id)
    if request.method == 'POST':
        if plane:
            airplane_form = AirplaneForm(request.POST,instance=plane)
            if airplane_form.is_valid():
                airplane_form.save()
                return redirect('airplane_page')


    else:        
        airplane_form = AirplaneForm(instance=plane)
        
        airplanes = Airplane.objects.all()
        
        context = {
            'form': airplane_form,
            'airplanes': airplanes
        }        

        return render(request,'edit_passenger.html',context)

def sign_up_view(request):
    message = ''
    if request.method == 'POST':
        sign_up_form = UserCreationForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            message = "Sign Up Successful"
        else:
            message = "Error in Sign Up"    
            return redirect('login_page')
    else:
        sign_up_form = UserCreationForm()
        
    context = {
        'form': sign_up_form,
        'message': message
    }        
    return render(request,'registration/sign_up.html',context) 

def dashboard_view(request):
    return render(request,'base.html')

def login_view(request):
    if request.method =='POST':
        form =LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect ('dashboard_page')
    else:
        form =LoginForm()

    return render(request,'registration/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('home_page')