"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('chatbot/',include('myapp.urls')),
    path('snake/',include('myapp.urls')),
    path('playgame/',include('myapp.urls')),
    path('play_space/',include('myapp.urls')),
    #path('login/',include('myapp.urls')),
    #path('sign_up/',include('myapp.urls')),
    #path('logout/',include('myapp.urls')),
    path('fortunecookie/',include('myapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user_login/',include('myapp.urls')),
    path('test_form/',include('myapp.urls')),

    
]
