n = int(input())
arreglo1 = []
arreglo2 = []

for i in range(n * 2):
    valor = int(input())
    
    if i % 2 == 0:
        arreglo1.append(valor)
    else:
        arreglo2.append(valor)
      
suma_minimos = min(arreglo1) + min(arreglo2)
print(suma_minimos)