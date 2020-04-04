q=1
w=1
while(q<=w):
    print("Elija el deporte de su preferencia: ")
    print("1- BASKETBALL")
    print("2- FUTBOL")
    print("3- VOLEY FEMENINO")
    print("4- VOLEY MASCULINO")
    disc = int(input("Ingrese el deporte: "))
    if(disc==1):
            i=1
            k=1
            while(i<=k):

                n=input("Ingrese su nombre:")

                e=int(input("Ingrese edad: "))
                if(e>=18):
                    r=1
                else:
                    r=0

                t=int(input("Ingrese estatura: "))
                if(t>=180):
                    rr=1
                else:
                    rr=0

                p=int(input("Ingrese el peso: "))
                if(p<=80):
                    rrr=1
                else:
                    rrr=0

                j=1
                if(j==r and j==rr and j==rrr):
                    print("Bienvenido",n," calificaste")
                else:
                    print("Lamentablemente no puedes calificar")

                z=int(input("¿Desea repetir proceso? 1=SI / 2=NO"))
                if(z==1):
                    k=k+1
                else:
                    k=0
            ff=int(input("¿Desea volver a elegir disciplina? 1=SI / 2=NO"))
            if(ff==1):
                w=w+1
            else:
                w=0
    elif(disc==2):
            i = 1
            k = 1
            while (i <= k):

                n = input("Ingrese su nombre:")

                e = int(input("Ingrese edad: "))
                if (e >= 15):
                    r = 1
                else:
                    r = 0

                t = int(input("Ingrese estatura: "))
                if (t >= 170):
                    rr = 1
                else:
                    rr = 0

                p = int(input("Ingrese el peso: "))
                if (p <= 70):
                    rrr = 1
                else:
                    rrr = 0

                j = 1
                if (j == r and j == rr and j == rrr):
                    print("Bienvenido", n, " calificaste")
                else:
                    print("Lamentablemente no puedes calificar")

                z = int(input("¿Desea repetir proceso? 1=SI / 2=NO"))
                if (z == 1):
                    k = k + 1
                else:
                    k=0
            ff = int(input("¿Desea volver a elegir disciplina? 1=SI / 2=NO"))
            if (ff == 1):
                w = w + 1
            else:
                w=0
    elif(disc==3):
            i = 1
            k = 1
            while (i <= k):

                n = input("Ingrese su nombre:")

                e = int(input("Ingrese edad: "))
                if (e <= 17):
                    r = 1
                else:
                    r = 0

                t = int(input("Ingrese estatura: "))
                if (t >= 175):
                    rr = 1
                else:
                    rr = 0

                p = int(input("Ingrese el peso: "))
                if (p <= 75):
                    rrr = 1
                else:
                    rrr = 0

                j = 1
                if (j == r and j == rr and j == rrr):
                    print("Bienvenido", n, " calificaste")
                else:
                    print("Lamentablemente no puedes calificar")

                z = int(input("¿Desea repetir proceso? 1=SI / 2=NO"))
                if (z == 1):
                    k = k + 1
                else:
                    k=0
            ff = int(input("¿Desea volver a elegir disciplina? 1=SI / 2=NO"))
            if (ff == 1):
                w = w + 1
            else:
                w=0
    elif(disc==4):
            i = 1
            k = 1
            while (i <= k):

                n = input("Ingrese su nombre:")

                e = int(input("Ingrese edad: "))
                if (e <= 18):
                    r = 1
                else:
                    r = 0

                t = int(input("Ingrese estatura: "))
                if (t >= 180):
                    rr = 1
                else:
                    rr = 0

                p = int(input("Ingrese el peso: "))
                if (p <= 80):
                    rrr = 1
                else:
                    rrr = 0

                j = 1
                if (j == r and j == rr and j == rrr):
                    print("Bienvenido", n, " calificaste")
                else:
                    print("Lamentablemente no puedes calificar")

                z = int(input("¿Desea repetir proceso? 1=SI / 2=NO"))
                if (z == 1):
                    k = k + 1
                else:
                    k=0
            ff=int(input("¿Desea volver a elegir disciplina? 1=SI / 2=NO"))
            if(ff==1):
                w=w+1
            else:
                w=0