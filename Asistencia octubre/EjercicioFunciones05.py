# ejercicio 5: convertidor de temperaturas
# realizar funciones para convertir de grados a celsius
# a fahrenheit y viseversa
# investigar la formula

#funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32 # la presedencia: multiplicacion,division y suma
#funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return  (fahrenheit -32) * 5/9  # respetar la presendencia utilizando parentesis

celsius= float(input('digite el valor de celsius: '))
resultado =celsius_fahrenheit(celsius)
print(f'{celsius} C A F ->{resultado:.2f}')

fahrenheit= float(input('digite el valor de fahrenheit : '))
resultado= fahrenheit_celsius(fahrenheit)

print(f'{fahrenheit} F A C->{resultado:.2f}')
