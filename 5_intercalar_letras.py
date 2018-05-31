texto = input()
intercalado = ''

# post o al indice % 2 == 0 para saber si espar

# range(4)     [0, 4>
# range(1, 4)  [1, 4>
# range(2,4,2) [2, 4> saltando 2

for i in range(0, len(texto) - 1, 2):
    if i % 2 == 0:
        intercalado += texto[i + 1] # intercalado = intercalado + texto[i + 1]
        intercalado += texto[i]

if len(texto) % 2 == 1:
    intercalado += texto[-1]

print(intercalado)

# iterar longitud texto, intercambiar de 2 en 2
# i debe sumar de 2 en 2
# cuando longitud es par
#   n / 2 iteraciones
#     digamos 6 ('Palabr')
#                 0 2 4 
# cuando longitud es impar
#   n / 2 + 1 iteraciones
#     digamos 7 ('Palabra')
#                 0 2 4 6
#                 aPalrba

# forzamos a que sean par para que no ocurra out of range


# 1234567  pos    "natural"
# 0123456  indice -- propio del for
# Palabra
# aPalrba


#          0123456
# texto = 'Palabra'
# iteracion Silaba   intercalada         intercalado      posicion para intercalar
# 0             Pa     aP                      1
# 2             la     aPal                    3
# 4             br     aPalrb                  5
# excluye con el -1, cuando len(texto, 7) 
# 5             a      aPalrba                 7 NO EXISTE   

#aPalrba

#if algo % 2 == 0:

#else:
#    impar