# Homework practico 2 Variables
#1.Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
variable_1 = 48
print(variable_1)


#2.Imprimir el tipo de dato de la constante 8.5
constante_1 = 8.5
print(type(constante_1))


#3.Imprimir el tipo de dato de la variable creada en el punto 1
print(type(variable_1))


#4.Crear una variable que contenga tu nombre
name = 'Fernando Mubarqui'


#5.Crear una variable que contenga un número complejo
Complejo_1 = 2 + 3j


#6.Mostrar el tipo de dato de la variable crada en el punto 5
print(type(Complejo_1))


#7.Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
num_pi = 3.1415


#8.Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
variable_8_1 = 'True'
variable_8_2 = True
print('La primera es una cadena string, la segunda es booleana')


#9.Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(variable_8_1))
print(type(variable_8_2))


#10.Asignar a una variable, la suma de un número entero y otro decimal
num_10_1 = 8
num_10_2 = 10.2
resultado_10 = num_10_1 + num_10_2
print(  resultado_10)


#11.Realizar una operación de suma de números complejos
complejo_11_1 = 1 + 3j
complejo_11_2 = 3 + 10j
print(complejo_11_1 + complejo_11_2)


#12.Realizar una operación de suma de un número real y otro complejo
num12 = 34
com12 = 2 +4j
resultado12 = num12 + com12
print(resultado12)


#13.Realizar una operación de multiplicación
num13_1 = 4
num13_2 = 3
multi13 = num13_1 * num13_2


#14.Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)


#15.Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente = 27/4
print(cociente)


#16.De la división anterior solamente mostrar la parte entera
entera = 27//4
print(entera)
 

#17.De la división de 27 entre 4 mostrar solamente el resto
resto = 27%4 
print(resto)


#18.Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
num18 = (entera * 4) + resto
print('Resultado Ejercicio 18 = ',num18)


#19.Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
variable19_1 = 'Es la cobra'
variable19_2 = ' TAKA TAKA'
print(variable19_1 + variable19_2)


#20.Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
variable20_1 = "2"
variable20_2 = 2
variable20_3 = variable20_1 == variable20_2
print(variable20_3)


#21.Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
variable21 = int(variable20_1) == variable20_2
print(variable21)


#22.¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
print('Porque los decimales se escriben con punto y la coma es para separar numeros')


#23.Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
variable23 = 3
print(variable23)
variable23-=1
print(variable23)


#24.Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
variable24 =1
variable24<<=2
print(variable24)
print('El operador corre 2 posiciones binarias el 1 quedando 100 binario que es 4 decimal')


#25.Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
print('No son del mismo tipo,uno es entero el otro un caracter')


#26.Realizar una operación válida entre valores de tipo entero y string
variable26_1 = 2
variable26_2 = '2'
print(variable26_1 * variable26_2)