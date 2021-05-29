#local
import time
print (" Ejemplo local")
print (" Vamos a realizar una suma")
print ("Ingresa un primer valor:")
N1 = int (input(""))
print ("************************")
print ("Ingresa un segundo valor:")
N2 = int (input(""))
print ("*************************")
SUMA=N1+N2
print ("Suma de Valores ingresados:")
print (SUMA)
print ("**************************")
time.sleep(5)


# optimizado
print (" Ejemplo local optimizado ")
print (" Vamos a realizar una suma")
print ("Ingresa un primer valor:")
N1 = int (input(""))
print ("Ingresa un segundo valor:")
N2 = int (input(""))
SUM=N1+N2
print ("Suma de Valores ingresados:")
print (SUM)

#-global 
print (" Ejemplo local")
print (" Vamos a contar letras ")
print("---------------------------------")
palabra=input("Ingrese una palabra ")
print("")
print("Cantidad de letras de la palabra")
print(len(palabra))
print("---------------------------------")

#optimizado
print (" Ejemplo local optimizado ")
print (" Vamos a contar letras ")
print("---------------------------------")
palabra=input("Ingrese una palabra ")
print("Cantidad de letras de la palabra ")
print(len(palabra))

# #ciclos
print (" Ejemplo ciclos ")
print("---------------------------------")
palab=input("Ingrese una palabra ")
print(palab)  
vocales="aeiou"  
def vocal(palab):  
  if palab in vocales:  
   print(palab," La palabra empieza con vocal.")  
  else:  
   print(palab," La palabra no empieza con vocal")  
vocal(palab)  

#optimizado
print (" Ejemplo ciclos optimizado ")
palab=input(" Ingrese una palabra ")
if palab[0]=="a" or palab[0]=="e" or palab[0]=="i" or palab[0]=="o" or palab[0]=="u":
    print(" La palabra ingresada comienza con vocal")
else:
    print(" La palabra ingresada no comienza con vocal")



#---------------------------
#global
print (" Ejemplo global ")
saludo = 'holaaaaaaaaaaaaaa' 
print(saludo)


#optimizado
print (" Ejemplo global optimizado ")
 #esta variable local pertenece al ámbito local de la función saludar
print("holaaaaaaaaaaaaaaaaaaaaaa")

#----------------------------
#global
print (" Ejemplo global ")
variable = 5
def f():
    var = variable
    print(var)
f()  
print (" Ejemplo global optimizado ")
#optimizado
variable = 5
print(variable)
 
 #---------------------
#global
print (" Ejemplo global ")
print("Nombres")
nombre1=" Julia "
print(nombre1)
nombre2=" Grissel "
print(nombre2)
nombre3=" Monica "
print(nombre3)
nombre4=" Francia "
print(nombre4)

#optimizado
print (" Ejemplo global optimizado ")
lista=[" Julia "," Grissel "," Monica "," Francia "]
print(lista)
        
#------------------
#ciclo
print (" Ejemplo ciclio ")
i=1
while i <= 10:
    print(i)
    i = i + 1
print("fin.")



# optimizado
print (" Ejemplo ciclo optimizado ")
i=1
while (i<=10):
    print(i)
    i+=1

#----------------
#local
print (" Ejemplo local ")

def nacio():
  nom=" C Ronaldo "
  ciud=" Portugal "  
  print("Nuestro amigo {} nació en {}.".format(nom,ciud))  
nacio()  


#optimizado
print (" Ejemplo local optimizado ")
nombre=" C Ronaldo " 
ciudad="Madrid"  
print("Nuestro amigo {} nació en {}.".format(nombre,ciudad))

#ciclo
print (" Ejemplo ciclo ") 
email=input("Ingrese un correo electronico ")
cantidad=0
x=0
while x<len(email):
    if email[x]=="@":
        cantidad=cantidad+1
    x=x+1
if cantidad==1:
    print("Contiene solo un caracter @ el correo ingresado")
else:
    print("Incorrecto")

#optimizado
print (" Ejemplo ciclo optimizado ")
mail=input("Ingrese un correo:")
cantidad=0
x=0
while x<len(mail):
    if mail[x]=="@":
        cantidad=cantidad+1
x=x+1
if cantidad==1:
    print("Contiene solo un caracter @ el correo ingresado")

#----------------------------------
# global
print (" Ejemplo global ")
def felicitar():
	print(felicitacion)
felicitacion = 'Felicidades feliz cumpleaños'
felicitar()


#optimizado
print (" Ejemplo global optimizado ")
felicitacion = 'Felicidades feliz cumpleaños'
print(felicitacion)

#-----------------------------------
  
print('FELIPE NERI BALAM CANUL') 