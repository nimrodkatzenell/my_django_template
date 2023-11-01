from django.shortcuts import render

# Create your views here.
def my_view(request):
    return render(request, 'test.html')

def view_chat(request):
    return render(request,'chatbot.html')

def view_snake(request):
    return render(request,'snake.html')
