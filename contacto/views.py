from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_Contacto=FormularioContacto()

    if request.method=="POST":
        formulario_Contacto=FormularioContacto(data=request.POST)
        if formulario_Contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde app django", 
            "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n{}".format(nombre,email,contenido),
            "",["gutycandiama@gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?Exitoso")
            except:
                return redirect("/contacto/?NoExitoso")

    return render(request,"contacto/contacto.html",{'miFormulario':formulario_Contacto})