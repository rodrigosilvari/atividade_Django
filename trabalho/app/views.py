from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render (request, 'index.html')

def noticias(request):
    ListaDeNoticias = ['politica', 'esporte', 'saude', 'dia-a-dia']

    return render (request, 'noticias.html')

def redatores(request):
    return render (request, 'redatores.html')