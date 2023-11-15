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
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
import http.client
import re
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import InputForm
from .forms import testForm




def user_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "user_login.html", context)

def test_form_view(request):
    context = {'form':testForm()}
    return render(request,'test_form.html',context)







# Create your views here.
def my_view(request):
    return render(request, 'home.html')

def view_chat(request):
    return render(request,'chatbot.html')

def view_snake(request):
    return render(request,'snake.html')
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def view_fortunecookie(request):

    conn = http.client.HTTPSConnection("fortune-cookie2.p.rapidapi.com")

    headers = {
    'X-RapidAPI-Key': "7908e910e1msh6c75498cb9b8e23p115698jsna353a46c3ccd",
    'X-RapidAPI-Host': "fortune-cookie2.p.rapidapi.com"
    }

    conn.request("GET", "/fortune", headers=headers)

    res = conn.getresponse()
    data = res.read()
    
    return HttpResponse(data.decode("utf-8"))

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


def logged_out(request):
    # Perform logout actions if necessary
    # Redirect to the home page after logout
    logout(request)
    return redirect('home.html') 




    

    
