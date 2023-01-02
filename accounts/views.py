from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from .forms import CustomersForm

# Create your views here.

def register(request):
    context = {'form': UserCreationForm}
    if request.method == 'POST':
        
        form_filled = UserCreationForm(request.POST)

        if form_filled.is_valid():

            form_filled.save()
           

            u_username = form_filled.cleaned_data['username']
            u_password = form_filled.cleaned_data['password1']



            user = authenticate(username = u_username, password = u_password)

            if user:
                login(request, user)
                return redirect('update_user')
            else:
                print("User not authenticated")
        
        else:

            return render(request, 'register.html', {'form': form_filled})

    return render(request, 'register.html', context)



def user_login(request):

    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == 'POST':

        u_username = request.POST.get('username')
        u_password = request.POST.get('password')

        user = authenticate(username = u_username, password = u_password)

        if user:
            login(request, user)
            next = request.GET.get('next', 'homepage')
            return redirect(next)
        else:
            context = {'form': AuthenticationForm(request.POST)}
            messages.add_message(request, messages.WARNING, "User not authenticated!")
            return render(request, 'login.html', context)

    else:
        context = {'form': AuthenticationForm}
        return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def profile_user(request):


    if request.user.is_superuser:
        return redirect('homepage')  
    elif request.user:
        profile = request.user.customer
    context = {'profile' : profile}
    return render(request, 'profile_user.html', context)


@login_required(login_url='login')
def update_user(request):

    profile = request.user.customer
    form = CustomersForm(request.POST or None,instance=profile)

    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('profile_user')
    
    return render(request, 'update_user.html', context)



