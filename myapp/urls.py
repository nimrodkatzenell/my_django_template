from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.my_view,name="my-view"),
    path('chatbot/',views.view_chat,name="chatbot"),
    path('snake/',views.view_snake,name="snake")

    

    # Additional URL patterns here
]
