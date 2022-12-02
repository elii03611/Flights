from django.urls import path

from .views import Homepage1, Homepage2, homepage

urlpatterns = [
    
    path('homepage/', homepage, name='staff_homepage'),
    path('homepage1/', Homepage1.as_view(), name='staff_homepage1'),
    path('homepage2/', Homepage2.as_view(), name='staff_homepage2'),


]




# Why use:
# - code quality
# - reliability

# - less time

# - debugging 

# - system integration

# Why not use:
# - hackaton
# - POC - prototype 