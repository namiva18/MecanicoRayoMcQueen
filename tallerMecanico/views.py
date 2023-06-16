from django.shortcuts import render


# Create your views here.
def index(request):
    context={}
    return render(request, 'tallerMecanico/index.html', context)

def quiensomos(request):
    context={}
    return render(request, 'tallerMecanico/quiensomos.html', context)

def trab_real(request):
    context={}
    return render(request, 'tallerMecanico/trab_real.html', context)

def caja_cambio(request):
    context={}
    return render(request, 'tallerMecanico/caja_cambio.html', context)

def electro(request):
    context={}
    return render(request, 'tallerMecanico/electro.html', context)

def suspension(request):
    context={}
    return render(request, 'tallerMecanico/suspension.html', context)

def contacto(request):
    context={}
    return render(request, 'tallerMecanico/contacto.html', context)

def login(request):
    context={}
    return render(request, 'tallerMecanico/login.html', context)
                  
def plantilla(request):
    context={}
    return render(request, 'tallerMecanico/plantilla.html', context)

def registro(request):
    context={}
    return render(request, 'tallerMecanico/registro.html', context)

                  