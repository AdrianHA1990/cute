from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 
from Cute_paginas.views import *
from django.contrib.staticfiles.urls import static

app_name = "app_cute"

urlpatterns = [
    path('', Inicio.as_view(), name="inicio"),
    path('cajas/', Cajas.as_view(), name="cajas"),
    path('arreglos/', Arreglos.as_view(), name="arreglos"),
    path('fotos/', Fotos.as_view(), name="fotos"),
    path('otros/', Otros.as_view(), name="otros"),
    path('contacto/', Contactanos.as_view(), name="contacto"),
    path('cotiza/', Cotiza, name="cotiza"),
    path('flork/', Flork.as_view(), name="flork"),
    path('jersey/', Jersey.as_view(), name="jersey"),
    path('dulcero/', Dulcero.as_view(), name="dulcero"),
    path('lunchbox/', Lunchbox.as_view(), name="lunchbox"),
    path('cajafotos/', Cajafotos.as_view(), name="cajafotos"),
    path('cajahex/', Cajahex.as_view(), name="cajahex"),
    path('logo/', Logo.as_view(), name="logo"),
    path('cajalet/', Cajalet.as_view(), name="cajalet"),
    path('letra/', Letra.as_view(), name="letra"),
    path('figuradul/', Figura.as_view(), name="figuradul"),
    path('figurapersonal/', FiguraP.as_view(), name="figurapersonal"),
    path('arreglobasico/', ArregloBasico.as_view(), name="arreglobasico"),
    path('arreglotematico/', ArregloTematico.as_view(), name="arreglotematico"),
    path('arregloburbuja/', ArregloBurbuja.as_view(), name="arregloburbuja"),
    path('arreglogigante/', ArregloGigante.as_view(), name="arreglogigante"),
    path('fotoscuadradas/', FotoCuadrada.as_view(), name="fotoscuadradas"),
    path('fotocolor/', FotoColor.as_view(), name="fotocolor"),
    path('fotoinsta/', FotoInsta.as_view(), name="fotoinsta"),
    path('fotorecta/', FotoRecta.as_view(), name="fotorecta"),
    path('fotocarta/', FotoCarta.as_view(), name="fotocarta"),
    path('mariposas/', Mariposas.as_view(), name="mariposas"),
    path('ramoper/', RamoPerso.as_view(), name="ramoper"),
    path('popup/', PopUp.as_view(), name="popup"),
    path('globoper/', GloboPer.as_view(), name="globoper"),
    path('globoled/', GloboLed.as_view(), name="globoled"),
    path('desayuno/', Desayuno.as_view(), name="desayuno"),
    path('ramopan/', RamoPan.as_view(), name="ramopan"),
    path('porta/', Porta.as_view(), name="porta"),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)