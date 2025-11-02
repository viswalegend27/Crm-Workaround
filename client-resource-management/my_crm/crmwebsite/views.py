from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Employee

def home(request):
    employee_rec= Employee.objects.all()
    
    if request.method == 'POST': 
        username = request.POST['username']  
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")  
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':employee_rec})

def logout_user(request):
    logout(request)  
    messages.success(request, "You have been logged out successfully.")
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
            messages.success(request, "You have sucessfully Registerd")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html',{'form':form})
    return render(request, 'register.html',{'form':form})

def employee_record(request, pk):
    if request.user.is_authenticated:
        emp_record = Employee.objects.get(id=pk)
        return render(request, 'record.html',{'emp_record':emp_record})
    else:
        messages.success(request, "You must be logged in!")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        deleted = Employee.objects.get(id=pk)
        deleted.delete()
        messages.success(request, "Record deleted!")
        return redirect('home')
    else:
        messages.success(request, "Must be logged in")
        return redirect('home')