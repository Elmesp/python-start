texto = input()
contador = [0, 0, 0, 0, 0]
#           a  e  i  o  u

for letra in texto:
    if letra == 'A' or letra == 'a':
        contador[0] += 1
    elif letra == 'E' or letra == 'e':
        contador[1] += 1
    elif letra == 'I' or letra == 'i':
        contador[2] += 1
    elif letra == 'O' or letra == 'o':
        contador[3] += 1
    elif letra == 'U' or letra == 'u':
        contador[4] += 1

print('a={0}, e={1}, i={2}, o={3}, u={4}'.format(contador[0],contador[1],contador[2],contador[3],contador[4]))