texto = input()
resultado = ''

for i in range(0, len(texto) - 1, 2):
    if i % 2 == 0:
        resultado += texto[i + 1]
        resultado += texto[i]

if len(texto) % 2 == 1:
    resultado += texto[-1]
    
print(resultado)