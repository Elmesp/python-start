nInput = input()
n = int(nInput)

for i in range(0, n):
    numeros = n - i
    linea = ''
    
    for j in range(0, numeros):
        if (i + j) % 2 == 0:
            linea += '1'
        else:
            linea += '0'

    print(linea)