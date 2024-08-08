"""Vista de Votos"""
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegistroForm, JugadorForm

# Create your views here.

def user_login(request):
    """Login user"""
    print(request.method)
    context = {}
    if request.method=="POST":
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=user_name, password=password)
        if user:   #Crear Session
            login(request, user)
            return redirect('juego')
        else:
            context["error"] = "User or Password incorrect"
            messages.error(request,"Usuario o Contraseña Incorrecta")
            return redirect('user_login')
    else:
        context['form'] = LoginForm()
        context['form_add'] = RegistroForm()
        context['form_jugador'] = JugadorForm()
        return render(request,'usuarios/login.html', context)


def user_logout(request):
    """Logout USER"""
    logout(request)
    return redirect('user_login')

def add_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print("Formulario")
            print("Usuario Creado")
            return redirect('user_login')
    else:
        return redirect('user_login')
