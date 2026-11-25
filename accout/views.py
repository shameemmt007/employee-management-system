
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import AdminSignupForm


def signup(request):

    admin_group, created = Group.objects.get_or_create(
        name='EmployeeAdmin'
    )

    # Allow only the first admin registration
    if admin_group.user_set.exists():
        messages.error(request, "Admin account already exists.")
        return redirect('login')

    if request.method == 'POST':
        form = AdminSignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.groups.add(admin_group)

            messages.success(
                request, "Account created successfully!"
            )
            return redirect('login')
    else:
        form = AdminSignupForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            if user.groups.filter(name='EmployeeAdmin').exists():
                login(request, user)
                return redirect('dashboard')

            messages.error(request, "You are not authorized as admin.")

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')


    


