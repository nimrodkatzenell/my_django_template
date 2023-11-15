from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.utils.translation import gettext_lazy as _










class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    mail = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))





class InputForm(forms.Form):
 
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput())
    
    
    
class testForm(forms.Form):
    SUBJECT_CHOICES = ((1,'web'),(2,'django'))
    name = forms.CharField(max_length = 200)
    age = forms.IntegerField()
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    date_of_birth = forms.DateField()
    
    