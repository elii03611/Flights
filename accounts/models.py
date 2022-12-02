from django.contrib.auth.models import Group, User
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
# from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customers', null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    # country = models.CountryField(null= True)
    email = models.EmailField(unique=True, null=True)
    phone_number = PhoneNumberField(unique=True)
    credit_card_no = models.CharField(max_length=50,unique=True)




  
    def __str__(self):
        return f"First Name: {self.first_name}, Last Name: {self.last_name}"


    def get_absolute_url(self):
        return reverse('customer_detail', args=[self.id])


def post_visitor_group(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.is_staff:
            Customer.objects.create(user_id = instance.id)
            Group.objects.get(name='Users').user_set.add(instance)
        else:
            Group.objects.get(name='Staff').user_set.add(instance)
        # else:
        #     Group.objects.get(name='Adminstrator').user_set.add(instance)

post_save.connect(receiver=post_visitor_group, sender=User)


class Adminstrator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE,null = True)





