from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request,'login.html')

def home_view(request):
    return render(request,'home.html')

def airline_view(request):
    return render(request,'airline.html')

def airplane_view(request):
    return render(request,'airplane.html')

def airport_view(request):
    return render(request,'airport.html')

def flight_view(request):
    return render(request,'flight.html')

def passenger_view(request):
    return render(request,'passenger.html')

def seat_view(request):
    return render(request,'seat_class.html')