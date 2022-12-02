from django.urls import path
from .views import (

    search,
    create_flight,
    delete_flight,
    # list_flight,
    flight_detail,
    update_flight,
    create_ticket,
    

    CreateFlights,
    CreateAirlineCompanies,
    CreateCountries,
    CreateCustomers,
    FlightsList,
    AirlineCompaniesList,
    CustomersList,
    TicketsList,
    FlightsDetail,
    CustomerDetail,
    AirlineCompaniesDetail,
    
    
    
)
from company_airline import views

urlpatterns = [

    path('',search, name='homepage'),
    path('homepage/',search, name='homepage'),
    path('flights/',FlightsList.as_view(), name='flights'),
    path('order_flight/', create_flight, name='order_flight'),
    path('delete_flight/<flight_id>', views.delete_flight, name='delete_flight'),
    path('update_flight/<flight_id>', views.update_flight, name='update_flight'),
    path('flight_detail/<int:id>',views.flight_detail, name='flight_detail'),
    path('create_ticket/<str:userId>/<str:flightId>', views.create_ticket, name='create_ticket'),

    path('add_flights/',CreateFlights.as_view(), name='add_flights'),
    path('add_airline_companies/',CreateAirlineCompanies.as_view(), name='add_airline_companies'),
    path('add_customers/',CreateCustomers.as_view(), name='add_customers'),
    path('add_countries/',CreateCountries.as_view(), name='add_countries'),
    path('airline/',AirlineCompaniesList.as_view(), name='airline'),
    path('customers/', CustomersList.as_view(),name='customers'),
    path('tickets/', TicketsList.as_view(),name='tickets'),
    path('customer_detail/<int:pk>',CustomerDetail.as_view(), name='customer_detail'),
    path('airline_companies_detail/<int:pk>',AirlineCompaniesDetail.as_view(), name='airline_companies_detail'),


]
