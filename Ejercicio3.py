n = []
suma=0

mayor=0
while n != -1:
    n = input('Inserta un numero')
    n = int(n)
    if n!=-1:
        suma = suma +n
        if(n>mayor):
            mayor=n
print('la suma vale', suma)
print('la media vale', suma/len(n))
print('el mayor es el numero ', mayor)
