from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        
        # Authenticate
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There was An Error Logging In")    
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out ... ")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})

# def register_user(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
        
#         # Log form data for debugging (remove sensitive data)
#         print(50*'-')
#         print(f"Form data keys: {list(request.POST.keys())}")
#         print(f"Username: {request.POST.get('username', 'N/A')}")
#         print(f"Email: {request.POST.get('email', 'N/A')}")
#         print(50*'-')
        
#         if form.is_valid():
#             try:
#                 user = form.save()
#                 print(f"User created successfully: {user.username}")
                
#                 # Authenticate and login
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password1']
#                 user = authenticate(request, username=username, password=password)
                
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request, "You Have Successfully Registered! Welcome!")
#                     return redirect('home')
#                 else:
#                     print(f"Authentication failed for user: {username}")
#                     messages.error(request, "Registration successful but login failed. Please try logging in.")
#                     return redirect('login')
#             except Exception as e:
#                 print(f"Error during user creation: {str(e)}")
#                 messages.error(request, "An error occurred during registration. Please try again.")
#         else:
#             # Log all form errors
#             print("Form is not valid:")
#             for field, errors in form.errors.items():
#                 print(f"  {field}: {errors}")
            
#             # Show all errors to user
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     if field == '__all__':
#                         messages.error(request, f"{error}")
#                     else:
#                         messages.error(request, f"{field.replace('_', ' ').title()}: {error}")
#     else:
#         form = SignUpForm()
    
#     return render(request, 'register.html', {'form': form})