i=1
m=0
f=0
ipri=0
isec=0
isup=0
acumEP=0
acumES=0
acumESU=0
k=1
mayor=0
while(i<=k):

    e = int(input("Ingrese su edad: "))
    if (e < 1):
        k = k - 1
    else:
        k = k + 1
    if(e>mayor):
        mayor=e

    ii=1
    m=1
    while(ii==m):
        print("Elija su sexo: ")
        print("1- MASCULINO")
        print("2- FEMENINO")
        s=int(input("Ingrese su sexo: "))
        if(s==1):
            m=m+1
            ii=0
        elif(s==2):
            f=f+1
            ii=0
        elif(s>2):
            print("ERROR, INGRESE NUEVAMENTE")
            m=1
    iii=1
    mm=1
    while(iii==1):
        print("Elija su grado de instrucción: ")
        print("1- PRIMARIA")
        print("2- SECUNDARIA")
        print("3- SUPERIOR")
        g= int(input("Ingrese su grado de instrucción: "))
        if(g==1):
            ipri=ipri+1
            acumEP=acumEP+e
            iii=0
        elif(g==2):
            isec=isec+1
            acumES=acumES+e
            iii=0
        elif(g==3):
            isup=isup+1
            acumESU=acumESU+e
            iii=0
        elif(g>3):
            print("ERROR, INGRESE NUEVAMENTE")
            iii=1

    r=int(input("¿Desea repetir proceso? 1=SI / 2=NO"))
    if(r==1):
        k=k+1
    else:
        k=0


print("La mayor edad de todos es: ",mayor)
print("El promedio de edades en las personas con instrucción primaria es: ",acumEP/ipri)
print("El promedio de edades en las personas con instruccion secundaria es: ",acumES/isec)
print("El promedio de edades en las personas con instrucción superior es: ",acumESU/isup)
print("La cantidad de personas del sexo masculino es: ",m)
print("La cantidad de personas del sexo femenino es: ",f)