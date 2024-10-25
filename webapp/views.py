from django.shortcuts import render, redirect
from .forms import createUserForm, loginForm


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
            
    context = {'form':form}
    return render(request, 'webapp/register.html', context=context)