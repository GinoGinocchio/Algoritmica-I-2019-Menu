cont=0
cont2=0
suma=0
p=0
bul=True
while (bul==True):

  print("Elegir las siguientes opciones:")
  print("1:ingreso de datos del trabajador")
  print("2.-Calcular el % de sueldos")
  print("3.-calculo de pago total\n")
  print("0.-salir.\n")
  opcion=int(input())
  
  if (opcion==1):
    print("Coloque los datos de los 6 trabajadores")
    while p < 6:
      nombre = input("ingresa nombre del empleado: ")
      print("sueldo del empleado",p+1,",", nombre,":")
      sueldo=int(input())
      if ((sueldo >=1000) & (sueldo<=2000)):
        if ((sueldo >= 1000) & (sueldo < 1500)):
            cont=cont+1
        else:
          cont2=cont2+1
        suma=suma+sueldo
        p=p+1
      else:
        print("sueldo fuera de rango, ingrese otro monto")
  elif (opcion==2):
    print("pocentaje 1000-1500", (cont/6)*100)
    print("pocentaje 1500-2000", (cont2/6)*100)
  elif (opcion==3):
    print("sueldo entregado total", suma)
  elif (opcion==0): 
    bul=False



