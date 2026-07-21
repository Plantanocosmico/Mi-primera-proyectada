#Bueno aqui quería poner un poco de los conceptos que aprendi
#Funciones secundarias 
def saludo():
  print("Hola que tal xd")
  print("Bueno estaba con unos cursos y estaba aprendiendo estos conceptos de las clases ")
  print("Estoy aprendiendo python y hise este programa asi rapido para practicar")
  print("Asi que vamos a darle ", end="")
  

def sumatoria(edad):
  print("Voy a sumar a tu edad el numero que digas ")
  numusuario=float(input("Pon un numero: "))

  print(f"Aqui esta tu edad aumentada {numusuario + edad}")
  if(edad>0):
    return print("Eres humano")
  if(edad<0):
    return print("Nop eres humano")
  if(edad==0):
    return print("XDDDD")  

#Def principal 
def main():
  saludo()
  usuario=input("Cual es tu nombre?: ")
  edad=int(input("Cual es tu edad?: "))
  sumatoria(edad)

  print("Y ya eso es todo si ves esto funciono el codigo \"yupiii\" y si no no xd")






  
#Empieza todo el programa 
if __name__ =="__main__":
  main()
  



