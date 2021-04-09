Nombre=input("Ingresa tu nombre ")
ApellidoP=input("Ingresa tu apellido paterno ")
ApellidoM=input("Ingresa tu apellido materno ")
Nacimiento=input("Ingresa tu fecha de nacimiento (dd/mm/aaaa) ")
fecha=Nacimiento.split("/")
rfc=ApellidoP[0:2]+ApellidoM[0:1]+Nombre[0:1]+fecha[2][2::]+fecha[1]+fecha[0]
print(rfc.upper())