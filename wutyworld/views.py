from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import JuegoForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def holamundo(request):
    return HttpResponse("Hola mundo")

def home(request):
    return render(request,"home.html",{
        "msg":"Cibernetica de 4to semestre"
    })

def registro(request):
    if request.method == "GET":
        return render(request,"registro.html",{
        "form": UserCreationForm
    })
    else:
        #Aqui tenemos nuestro POST
        req=request.POST
        if req['password1']==req['password2']:
            try:
                user = User.objects.create_user(
                    username=req['username'],
                    password=req['password1']
                )
                user.save()
                login(request,user)
                return redirect("/")
            except IntegrityError as ie:
                return render(request,"registro.html",{
                    "form": UserCreationForm,
                    "msg": "Este usuario ya existe"
                })
            except Exception as e:
                return render(request,"registro.html",{
                    "form": UserCreationForm,
                    "msg": f"Hubo un error{e}"
                })
                
                
def iniciarSesion(request):
    if request.method=="GET":
        return render(request, "login.html",{
            "form": AuthenticationForm,
        })
    else:
        try:
            user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                return render(request, "login.html",{
                "form": AuthenticationForm,
                "msg": "El usuario o contraseña es incorrecto"
            })
        except Exception as e:
            return render(request, "login.html",{
                "form": AuthenticationForm,
                "msg": "Hubo un error{e}"
            })
            
def cerrarsesion(request):
    logout(request)
    return redirect("/")

@login_required
def nuevojuego(request):
    if request.method=="GET":
        return render(request, "nuevojuego.html",{
                    "form": JuegoForm
                })
    else:
        try: 
            form=JuegoForm(request.POST)
            if form.is_valid():
                nuevo=form.save(commit=False)
                if request.user.is_authenticated:
                    nuevo.usuario=request.user
                    nuevo.save()
                    return redirect("/")
                else:
                    return render(request, "nuevojuego.html",{
                        "form": JuegoForm,
                        "msg":"Debe de autenticarse"
                    })
            else:
                return render(request, "nuevojuego.html",{
                        "form": JuegoForm,
                        "msg": "Este juego no es valido"
                    })
        except Exception as e:
            return render(request, "nuevojuego.html",{
                        "form": JuegoForm,
                        "msg": f"Error de autenticacion{e}"
                    })
                    