from django.shortcuts import render, redirect
from .models import *
from .forms import MensajeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404

@login_required
def mensajes_lista(request):
    mensajes = Mensaje.objects.all()
    no_hay_mensajes = False
    
    if request.method == 'POST':
        mensaje_id = request.POST.get('mensaje_id')
        mensaje = get_object_or_404(Mensaje, id=mensaje_id)
        
        if mensaje.autor == request.user or request.user.is_superuser:
            mensaje.delete()
            
            if Mensaje.objects.count() == 0:
                no_hay_mensajes = True
                mensajes = None
    
    context = {'mensajes': mensajes, 'no_hay_mensajes': no_hay_mensajes}
    return render(request, 'MensajesApp/mensajes_lista.html', context)


#@login_required
#def crear_mensaje(request):
#    if request.method == 'POST':
#        contenido = request.POST['content']
#        autor = request.user
#        mensaje = Mensaje.objects.create(autor=autor, contenido=contenido)
#        return redirect('mensajes_lista')
#    return render(request, 'MensajesApp/crear_mensaje.html')

@login_required
def crear_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST, request.FILES)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.autor = request.user
            mensaje.save()
            return redirect('mensajes_lista')
    else:
        form = MensajeForm()
    
    context = {'form': form}
    return render(request, 'MensajesApp/crear_mensaje.html', context)
