#Flujos de Control
#1.Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
x = 0
if(x > 0):
    print('El numero', x, ' es mayor que 0')
elif(x < 0):
    print('El numero', x, ' es menor que 0')
else:
    print('El nuemro es cero')

#2.Crear dos variables y un condicional que informe si son del mismo tipo de dato
var1 = 'cadena'
var2 = '234'
if(type(var1) == type(var2)):
    print('Las variables son del mismo tipo')
else:
    print('Las variables son de distinto tipo')


#3.Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for a in range(1,21):
    res = a % 2
    if(res == 0):
        print('El numero ', a, ' es par')
    else:
        print('El numero ', a, ' es impar')


#4.En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for b in range(0, 6):
    res4 = b**3
    print('El resultado de ', b, ' es: ', res4)


#5.Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
var5 = 7
print('Los numeros son:')
for i in range(1, (var5+1)):
    print(i)

#6.Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

#7.Crear un ciclo for dentro de un ciclo while
var7 = 0
while(var7 < 7):
    for i in range(1, var7):
        print('El numero del while es:  ', var7)
        print('El numero del for es:    ', i)

    var7 += 1

#8.Crear un ciclo while dentro de un ciclo for

#9.Imprimir los números primos existentes entre 0 y 30
for j in range(0, 31):
    while(j >= 0):
        if(i > 0):
            i = j-1
        res9 = j % i
        if(res9 > 0)
            

#10.¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

#11.En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

#12.Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

#13.Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

#14.Utilizar la función input() que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

#15.Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6