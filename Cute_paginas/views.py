from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Clientes
# Create your views here.


class Inicio(TemplateView):
    template_name = 'inicio.html'
    
class Cajas(TemplateView):
    template_name = 'Paginas_Base/cajas.html'    
    
class Arreglos(TemplateView):
        template_name = 'Paginas_Base/arreglos.html'   
        
class Fotos(TemplateView):
        template_name = 'Paginas_Base/fotos.html'
class Otros(TemplateView):
        template_name = 'Paginas_Base/otros.html'

class Contactanos(TemplateView):
        template_name = 'Paginas_Base/contacto.html'

def Cotiza(request):
        if request.method == 'POST':
          nom = request.POST.get('nombre')
          tel = request.POST.get('telefono')
          cor = request.POST.get('correo')
          art = request.POST.get('articulo')
          esp = request.POST.get('especificaciones')
          dire = request.POST.get('direccion')
          comen = request.POST.get('comentarios')
          clien = Clientes(nombre=nom, telefono=tel, correo=cor, articulo=art, especificaciones=esp, direccion=dire, comentarios=comen)
          clien.save()
          return redirect('app_cute:inicio')
        return render(request, 'Paginas_Base/cotiza.html',)


class Flork(TemplateView):
        template_name = 'Paginas_Base/flork.html'   
        
class Jersey(TemplateView):
        template_name = 'Paginas_Base/jersey.html'
        
class Dulcero(TemplateView):
        template_name = 'Paginas_Base/dulcero.html'   
        
class Lunchbox(TemplateView):
        template_name = 'Paginas_Base/lunchbox.html'   
class Cajafotos(TemplateView):
        template_name = 'Paginas_Base/cajafotos.html'   
class Cajahex(TemplateView):
        template_name = 'Paginas_Base/cajahex.html'
class Logo(TemplateView):
        template_name = 'Paginas_Base/logo.html'  
class Cajalet(TemplateView):
        template_name = 'Paginas_Base/cajalet.html'
class Letra(TemplateView):
        template_name = 'Paginas_Base/letra.html'                  
class Figura(TemplateView):
        template_name = 'Paginas_Base/figuradul.html'  
class FiguraP(TemplateView):
        template_name = 'Paginas_Base/figurapersonal.html'   
         
class ArregloBasico(TemplateView):
        template_name = 'Paginas_Base/arreglobasico.html'    
        
class ArregloTematico(TemplateView):
        template_name = 'Paginas_Base/arreglotematico.html'  
class ArregloBurbuja(TemplateView):
        template_name = 'Paginas_Base/arregloburbuja.html'
class ArregloGigante(TemplateView):
        template_name = 'Paginas_Base/arreglogigante.html'  
        
class FotoCuadrada(TemplateView):
        template_name = 'Paginas_Base/fotoscuadradas.html'
class FotoColor(TemplateView):
        template_name = 'Paginas_Base/fotocolor.html'  

class FotoInsta(TemplateView):
        template_name = 'Paginas_Base/fotoinsta.html' 
class FotoRecta(TemplateView):
        template_name = 'Paginas_Base/fotorecta.html' 
        
class FotoCarta(TemplateView):
        template_name = 'Paginas_Base/fotocarta.html' 
                                        
class Mariposas(TemplateView):
        template_name = 'Paginas_Base/mariposas.html' 
        
class RamoPerso(TemplateView):
        template_name = 'Paginas_Base/ramoper.html'
class PopUp(TemplateView):
        template_name = 'Paginas_Base/popup.html'
class GloboPer(TemplateView):
        template_name = 'Paginas_Base/globoper.html' 
class GloboLed(TemplateView):
        template_name = 'Paginas_Base/globoled.html'
class Desayuno(TemplateView):
        template_name = 'Paginas_Base/desayuno.html'   
class RamoPan(TemplateView):
        template_name = 'Paginas_Base/ramopan.html'
class Porta(TemplateView):
        template_name = 'Paginas_Base/porta.html'                         
                                        