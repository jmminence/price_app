from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'autenticacion/login.html'

@login_required
def home(request):
    return render(request, 'autenticacion/home.html')

############################### EMPRESAS ######################################

def easy_view(request):
    return render(request, 'autenticacion/easy.html')

def arriservi_view(request):
    return render(request, 'autenticacion/arriservi.html')

def mct_view(request):
    return render(request, 'autenticacion/mct.html')