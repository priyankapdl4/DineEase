from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    
        un = request.POST.get('username')
        pw = request.POST.get('password1')
        pw2 = request.POST.get('password2')

        if pw != pw2:
            print('error not matching password')
            messages.error(request, 'password don\'t match, try again')
            return redirect(request.path)

        elif(User.objects.filter(username=un).exists()):
            print('error userid already exist')
            messages.error(request, 'User Already Exists, try other unique username')
            return redirect(request.path)

        else:
            new_user = User(username=un)
            new_user.set_password(pw)
            new_user.save()
            messages.success(request, 'Account Created Successfully, You can Login Now')
            return HttpResponseRedirect('/login/')
     
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/order')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'accounts/dashboard.html', {'user': request.user})
