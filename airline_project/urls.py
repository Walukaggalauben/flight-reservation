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
from Airline.views import edit_airplane,deleteairplane,login_view,home_view,airline_view,airplane_view,airport_view,flight_view,passenger_view,seat_view,edit_passenger,delete_passenger,edit_flight,delete_flight,delete_seat_class,edit_seat_class,delete_airport,edit_airport,delete_airline,edit_airline

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',login_view,name = 'login_page'),
    path('homepage/',home_view,name = 'home_page'), 
    path('airlinepage/',airline_view,name = 'airline_page'),
    path('airplanepage/',airplane_view,name ='airplane_page'),
    path('airportpage/',airport_view,name ='airport_page'),
    path('flightpage/',flight_view,name ='flight_page'),
    path('passengerpage/',passenger_view,name ='passenger_page'),
    path('seatpage/',seat_view,name ='seat_page'),
    path('delete_passenger/<int:passenger_id>/',delete_passenger,name ='delete_passenger_page'),
    path('edit_passenger/<int:passenger_id>/',edit_passenger,name ='edit_passenger_page'),
    path('delete_airplane/<int:airplane_id>/',deleteairplane,name ='delete_airplane_page'),
    path('edit_airplane/<int:airplane_id>/',edit_airplane,name ='edit_airplane_page'),
    path('edit_flight/<int:flight_id>/',edit_flight,name ='edit_flight_page'),
    path('delete_flight/<int:flight_id>/',delete_flight,name ='delete_flight_page'),
    path('delete_seat_class/<int:seat_class_id>/',delete_seat_class,name ='delete_seat_class_page'),
    path('edit_seat_class/<int:seat_class_id>/',edit_seat_class,name ='edit_seat_class_page'),
    path('delete_airport/<int:airport_id>/',delete_airport,name ='delete_airport_page'),
    path('edit_airport/<int:airport_id>/',edit_airport,name ='edit_airport_page'),
    path('delete_airline/<int:airline_id>/',delete_airline,name ='delete_airline_page'),
    path('edit_airline/<int:airline_id>/',edit_airline,name ='edit_airline_page'),
]
