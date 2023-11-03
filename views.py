from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import LoginForm # Replace . with the actual module path if needed
import subprocess
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home.html')  # Redirect to a success page or the home page
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})


# Create your views here.
def my_view(request):
    return render(request, 'home.html')

def view_chat(request):
    return render(request,'chatbot.html')

def view_snake(request):
    return render(request,'snake.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    
    
def play_game(request):
    # Start your Pygame script as a separate process
    subprocess.Popen(["python", "myapp/game_script.py"])
    return render(request, 'game_template.html')

def play_space(request):
    subprocess.Popen(["python", "myapp/space/Space-Invaders-Pygame/space.py"])
    text = "<h1> Pygame is running in another window. </h1>"
    return HttpResponse(text)

    

    
