from django.contrib import admin
from django.urls import path
from .views import CustomLoginView
from . import views
from .views import play_game


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.my_view,name="my-view"),
    path('chatbot/',views.view_chat,name="chatbot"),
    path('snake/',views.view_snake,name="snake"),
    path('login/', views.register, name='login'),
    path('sign_up/',views.signup,name="sing_up"),
    path('play_game/', views.play_game, name='play_game'),
    path('play_space/',views.play_space,name='play_space'),
    
    # Additional URL patterns here
]
