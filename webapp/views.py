from django.shortcuts import render, redirect
from .forms import createUserForm, loginForm

# for login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required # Allows only users that login to see the dashboard

# Home page
def home(request):
    return render(request, 'webapp/index.html')



# Register

def register(request):
    
    form = createUserForm
    if request.method == 'POST':
        form = createUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('mylogin')
            
    context = {'form':form}
    return render(request, 'webapp/register.html', context=context)


# Login user

def myLogin(request):
    
    form =loginForm()
    if request.method == 'POST':
        form = loginForm(request, data=request.POST) # send the data as entered in the login form
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None: #check if user exists
                auth.login(request, user)
                
                
                return redirect('dashboard')
    
    context = {'form':form}
    return render(request, 'webapp/mylogin.html', context=context)



# User Dashboard

@login_required(login_url='mylogin')  # Only users that login can see the dashboard
def dashboard(request):
    
    return render(request, 'webapp/dashboard.html')









# Logout User

def userLogout(request):
    auth.logout(request)
    
    return redirect('mylogin')