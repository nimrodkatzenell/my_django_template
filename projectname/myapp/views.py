from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import LoginForm # Replace . with the actual module path if needed
import subprocess
from django.http import HttpResponse


# Create your views here.
def my_view(request):
    return render(request, 'test.html')

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
    return HttpResponse("Pygame is running.")

    

    
