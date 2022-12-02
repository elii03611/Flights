from django.urls import path
from .views import (register, 
                    user_login, 
                    user_logout,
                    profile_user,
                    update_user
                    
                    )

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile_user/', profile_user, name='profile_user'),
    path('update_user/', update_user, name='update_user'),

]
