from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .models import Account
# Create your views here.

def register(request):
  if request.method == "POST":
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password').strip()
    confirm_password = request.POST.get('confirm_password').strip()

    ### password mathc check 
    if password != confirm_password:
      return render(request, 'register.html', {'error': 'password do not match'})
    
    ## Email already exists check
    if Account.objects.filter(email=email).exists():
      return render(request, 'register.html', {
        'error': 'Email already registered please Login'
      })
    
    ## Create user
    user = Account.objects.create_user(
      email = email,
      password = password
    )
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    return redirect('index')
  
  return render(request, 'register.html')



## ------- LogIn Views -----

def uuser_login(request):
  if request.method == "POST":
    email = request.POST.get('email').strip()
    password = request.POST.get('password').strip()

    # Authenticate user
    user = authenticate(request, email=email, password=password)

    if user is not None:
      login(request, user)
      return redirect('index')
    else:
      return render(request, 'login.html', {'error': 'Invalid email or password'})
    
  return render(request, 'login.html')



### ------------ Logout Views -------

def user_logout(request):
  logout(request)
  return redirect('login')
