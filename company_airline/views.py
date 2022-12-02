from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import FlightsForm
from .models import Airline_Companie, Countrie, Customer, Flight, Ticket
from django.http import HttpResponse
from django.db.models import Q
from datetime import date, datetime

# Create your views here.


    # reservations = user.visitor.reservations.all()
    # context['past_reservations'] = reservations.filter(check_out__lt = date.today())
    # context['future_reservations'] = reservations.filter(check_in__gt = date.today()).order_by('check_in')
    # context['current_reservations'] = reservations.filter(Q(check_in__gte = date.today()) & Q(check_out__gt = date.today()))


def search(request):
    flight = Flight.objects.all()

    airline_company = request.GET.get('airline_company_id')
    origin_country = request.GET.get('origin_country_id')
    destination_country = request.GET.get('destination_country_id')
    departure_time = request.GET.get('departure_time')
    landing_time = request.GET.get('landing_time')
    
    def is_valid_queryparam(param):
        return param != '' and param is not None
        
    qs = None    

    if is_valid_queryparam(airline_company):
        qs = flight.filter(airline_company__name__icontains = airline_company)  
    if is_valid_queryparam(origin_country):
        qs = qs.filter(origin_country__countries__icontains = origin_country)
    if is_valid_queryparam(destination_country):
        qs = qs.filter(destination_country__countries__icontains = destination_country)
    if  is_valid_queryparam(departure_time):
        qs = qs.filter(departure_time__icontains = departure_time)
    if is_valid_queryparam(landing_time):
        qs = qs.filter(landing_time__icontains = landing_time)

    context = {
        'queryset': qs
    }
    return render (request,'homepage.html', context)



@login_required
def create_flight(request):
    context = {'form': FlightsForm()}
    if 'flight' in request.GET:
                  
        number_tickets = request.session.get('number_tickets')
        airline_company = request.session.get('airline_company')
        origin_country = request.session.get('origin_country')
        destination_country = request.session.get('destination_country')
  
    if request.method == 'POST':

        form_filled = FlightsForm(request.POST)
        if form_filled.is_valid():
            airline_company = form_filled.cleaned_data['airline_company']
            origin_country = form_filled.cleaned_data['origin_country']
            destination_country = form_filled.cleaned_data['destination_country']
            number_tickets = form_filled.cleaned_data['number_tickets']



            flights = Flight.objects.filter(airline_company = airline_company, origin_country = origin_country, destination_country = destination_country).exclude(number_tickets = number_tickets <= 0)

            if flights.exists():
                request.session['airline_company'] = str (airline_company)
                request.session['origin_country'] = str(origin_country)
                request.session['destination_country'] = str(destination_country)



            return render(request,'available_flights.html', {'flights': flights})   
    return render(request, 'order_flight.html', context)


def create_ticket(request, userId, flightId):
    flight = Flight.objects.get(id=int(flightId))
    if flight.number_tickets > 0:

        user = User.objects.get(id=int(userId))
        customer = Customer.objects.get(user_id=user.id)
        t = Ticket(flight=flight, customer=customer)
        t.save()
        flight.number_tickets = flight.number_tickets - 1
        
        flight.save()
        return  HttpResponse (f'ticket number: [{t.id}] number flight: [{flight.id}] was added successfully, - You can see all the information on your flights')
    else:
        return HttpResponse(f'no ticket ')


@login_required
def flight_detail(request, id):
    f_detail = Flight.objects.get(pk = id)
    return render(request,'flight_detail.html',{'f_detail': f_detail})


@login_required
def update_flight(request, flight_id):
        flight = Flight.objects.get(pk = flight_id)
        form = FlightsForm(request.POST or None, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flights')
        return render(request, 'update_flights.html', {'flight': flight, 'form': form})
    

@login_required
def delete_flight(request, flight_id):
        flight = Flight.objects.get(pk = flight_id)
        if request.method == 'POST':
            flight.delete()
            return redirect('flights')
        return render(request, 'delete_flight.html')



class CreateFlights(CreateView):

    template_name = 'add_flights.html'
    form_class = FlightsForm
    success_url='../homepage'



class CreateCountries(CreateView):
    model = Countrie
    template_name = 'add_countries.html'
    fields='__all__'
    success_url='../homepage'

    
class CreateCustomers(CreateView):
    model = Customer
    template_name = 'add_customers.html'
    fields='__all__'
    success_url='../homepage'



class CreateAirlineCompanies(CreateView):
    model = Airline_Companie
    template_name = 'add_airline_companies.html'
    fields='__all__'
    exclude = ['customers']
    success_url='../homepage'

class FlightsList(ListView):
    
    model= Flight
    context_object_name= 'flights'
    template_name= 'flights.html'



class AirlineCompaniesList(ListView):
    
    model= Airline_Companie
    context_object_name= 'airline_companies'
    template_name= 'airline_companies.html'




class TicketsList(ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'tickets.html'


    def get_queryset(self,*args,**kargs):
        user = User.objects.get(username = self.request.user)
        customer = Customer.objects.get(user_id=user.id)
        all_ticket = super(TicketsList,self).get_queryset(*args,**kargs)
        user_ticket = all_ticket.filter(customer = customer)

        return user_ticket.all()


class CustomersList(ListView):
    
    model= Customer
    context_object_name= 'customers'
    template_name= 'customers.html'



    def get_queryset(self,*args,**kargs):
        user = User.objects.get(username = self.request.user)
        all_customers = super(CustomersList,self).get_queryset(*args,**kargs)
        user_customers = all_customers.filter(user = user)

        return user_customers.all()



class FlightsDetail(DetailView):
    model = Flight
    template_name = 'flight_detail.html'
    context_object_name = 'flight_detail'






class CustomerDetail(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customers'



class AirlineCompaniesDetail(DetailView):
    model = Airline_Companie
    template_name = 'airline_companies_detail.html'
    context_object_name = 'airline_companies'


