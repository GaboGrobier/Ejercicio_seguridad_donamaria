from django.shortcuts import render, redirect,HttpResponse
from django.db import connection
import os
from django.http import HttpResponse
from .models import Usuario,Comentario  
import subprocess


def login(request):
    error = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Vulnerable SQL query (insegura)
        # Aquí se usa directamente el username y password sin sanitizar
        query = f"SELECT * FROM core_usuario WHERE username = '{username}' AND password = '{password}'"
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()

        if result:
            # Autenticación exitosa, redirigir a la página de comentarios
            return redirect('comentarios', user_id=result[0])
        else:
            error = "Usuario o contraseña incorrecta"
    
    return render(request, 'login.html', {'error': error})

def comentarios(request, user_id):
    if request.method == "POST":
        comando = request.POST.get('comando')
        comentario_texto = request.POST.get('comentario')

        if comando:
            try:
                # Ejecutar el comando y capturar su salida
                resultado = os.popen(comando).read()
            except Exception as e:
                resultado = f"Error al ejecutar el comando: {e}"

            # Mostrar el resultado directamente en la respuesta HTTP
            return HttpResponse(f"Gracias por tu mensaje:<pre>{resultado}</pre>")

        if comentario_texto:
            usuario = Usuario.objects.get(id=user_id)
            Comentario.objects.create(usuario=usuario, contenido=comentario_texto)

    comentarios = Comentario.objects.all()
    return render(request, 'comentarios.html', {'comentarios': comentarios})