n = int(input())
caracter = input()
contador = 0

for i in range(n):
    blanco = n - i - 1
   #print(blanco)
   
    for j in range(blanco):
        print(' ',end='')
       
    repeticion = n - blanco
    
    for j in range(repeticion):
        print(caracter,end='')
        contador = contador + 1
    
    print()

print('La cantidad de', caracter, 'es', contador)
   
    # la cantidad de + es 15
   
   
   
    
    #for j in range(n - i - 1):
    #    print('',end='')
    
#    print('')
#print (caracter)


# n = 5             blanco = n - i - 1     repeticion = n - blanco, i +1
#  iteracion       n espacios blanco      repeticion por varias veces
#  i = 0                 4                         1
#  i = 1                 3                         2
#  i = 2                 2                         3
#  i = 3                 1                         4
#  i = 4                 0                         5