
from xml.dom import ValidationErr
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import Customer

# Create your models here.



class Countrie(models.Model):

    countries = CountryField(blank_label='select country',null= True)
    def __str__(self):
        
        return f" {self.countries.name}"


    




class Airline_Companie(models.Model):
    name = models.CharField(max_length=50,unique=True)
    country = models.ForeignKey(Countrie,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} "

    def get_absolute_url(self):
        return reverse('airline_companies_detail', args=[self.id])
    

class Flight(models.Model):
    airline_company = models.ForeignKey(Airline_Companie,on_delete=models.CASCADE,related_name='airline_company', null= True)
    origin_country = models.ForeignKey(Countrie,on_delete=models.CASCADE)
    destination_country = models.ForeignKey(Countrie,on_delete=models.CASCADE, related_name= 'destination', null= True)
    departure_time = models.DateTimeField(null=True)
    landing_time = models.DateTimeField(null=True)
    number_tickets = models.IntegerField(null=True,default=1,validators=[MinValueValidator(0),MaxValueValidator(200)])


    # def clean(self):
    #     if self.departure_time < self.landing_time:
    #         raise ValidationErr("Invalid date")
    
    
    def __str__(self):
        return f"""Airline Company: {self.airline_company}, - From: {self.origin_country}, - 
        To: {self.destination_country}, - Departure Time: {self.departure_time}, - Landing Time: {self.landing_time}"""
        

    def get_absolute_url(self):
        return reverse('flight_detail', args=[self.id])   


class Ticket(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer')

    def __str__(self):
        return f"{self.id}, - {self.flight}, - {self.customer}"
  

