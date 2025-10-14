"""
URL configuration for airline_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Airline.views import login_view,home_view,airline_view,airplane_view,airport_view,flight_view,passenger_view,seat_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',login_view,name = 'login_page'),
    path('homepage/',home_view,name = 'home_page'), 
    path('airlinepage/',airline_view,name = 'airline_page'),
    path('airplanepage/',airplane_view,name ='airplane_page'),
    path('airportpage/',airport_view,name ='airport_page'),
    path('flightpage/',flight_view,name ='flight_page'),
    path('passengerpage/',passenger_view,name ='passenger_page'),
    path('seatpage/',seat_view,name ='seat_page')
]
