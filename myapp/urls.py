from django.contrib import admin
from django.urls import path
from .views import CustomLoginView
from . import views
from .views import play_game
from django.contrib.auth import views as auth_views
from .views import SignUpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.my_view,name="home"),
    path('chatbot/',views.view_chat,name="chatbot"),
    path('snake/',views.view_snake,name="snake"),
    path('play_game/', views.play_game, name='play_game'),
    path('play_space/',views.play_space,name='play_space'),
    path('fortunecookie/',views.view_fortunecookie,name="fortunecookie"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('user_login',views.user_view,name = "user_login"),
    path('test_form',views.test_form_view,name="test_form"),
    #path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # Additional URL patterns here
    
]
