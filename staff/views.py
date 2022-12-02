from accounts.models import Customer, User
from company_airline.models import Airline_Companie
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

# Create your views here.

def homepage(request):
    return render(request, 'staff_homepage.html', {})





class Homepage1(TemplateView):
    template_name = 'staff_homepage1.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('search customers')
        if q:
            customers = Customer.objects.filter(Q(first_name__icontains = q) | Q(last_name__icontains = q))
            context['customers'] = customers
        return context
        

class Homepage2(TemplateView):
    template_name = 'staff_homepage2.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('search airline_companies')
        if q:
            airline_companies = Airline_Companie.objects.filter(name__icontains = q)
            context['airline_companies'] = airline_companies
            
        return context
