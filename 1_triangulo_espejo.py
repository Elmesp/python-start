# print('Ingrese tamaño: ')
tamanoInput = input()
tamano = int(tamanoInput)

# print('Ingrese caracter: ')
caracter = input()

for i in range(1, tamano + 1):
    espacios = tamano - i
    linea = ''
    
    for j in range(0, espacios):
        linea += ' '
    
    for j in range(0, i):
        linea += caracter
        
    print(linea)