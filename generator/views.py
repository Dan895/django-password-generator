from django.shortcuts import render
import random as rdm
# con esta libreria podemos mostrar texto de 
# la funcion about (solo es un ejemplo)
# lo que queremos de verdad es mostrar html
# from django.http import HttpResponse

# Create your views here.
# def about(request):
#   return HttpResponse('<h1>Hello</h1>')

# para mejorar el codigo comentado necesitamos
# crear una carpeta dentro de la app 'generator'
# llamada 'template' que tendra todo el html
# que necesitemos devolver al cliente

# El 'request' siempre va dentro de la funcion
def about(request):
  return render(request, 'generator/about.html')
  # hasta aqui sale un error, se debe a que el 
  # templeate no esta siendo encontrado
  # esto se debe a que en nuestra aplicacion
  # principal no le hemos dicho que la app 'generator' existe, para ello ir carpeta del proyecto (en este caso 'django_password_generator') -> settings.py -> buscar seccion INSTALLED_APPS

# El flujo es que recibe un request y renderiza
# la vista, en este caso home.html
def home(request):
  return render(request, 'generator/home.html')

def password(request):
  # aqui podemos ejecutar logica extra que se 
  # puede devolver
  chars = list('abcdefghijklmnopqrstuvwwxyz')
  generated_password = ''

  # para recibir la longitud desde la vista
  # (cualquier dato de la vista en realidad)
  # usamos 'request':
  # y lo mostramos por consola 
  # esta informacion la envia la barra de url
  # y esto es un string, para trabajar con la
  # propiedad que necesitamos la debemos parsear
  # print(request.GET.get('length'))
  length = int(request.GET.get('length'))
  
  if request.GET.get('uppercase'):
    chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
  if request.GET.get('special'):
    chars.extend(list('-_!@?'))
  if request.GET.get('numbers'):
    chars.extend(list('0123456789'))

  for char in range(length):
    generated_password += rdm.choice(chars)
  
  print("password length: ",len(generated_password))
  # esto aun no muestra la password generada
  # return render(request, 'generator/password.html')
   
  #haciendo un diccionario como se muestra a continuacion, si muestra la password generada,
  # pero necesita que la vista lo especifique 
  # para poder verlo (ver la vista)
  return render(request, 'generator/password.html', {'password':generated_password})