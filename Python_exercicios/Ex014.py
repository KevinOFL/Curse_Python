#Desafio conversão de temperatura.

celsius1 = float(input('Digite a temperatura em Celsius para a conversão em Fahrenheit: '))
fahrenheit = float(input('Digite a temperatura em Fahrenheit para a conversão em Celsius: '))
celsius2 = float(input('Digite a temperatura em Celsius para a conversão de Celsius para Kelvin: '))
kelvin = float(input('Digite a temperatura absoluta (em Kelvin) para a conversão de Kelvin para Celsius: '))

convFanr = celsius1 * 1.8 + 32
convCels1 = (fahrenheit - 32) / 1.8
convCels2 = celsius2 + 273.15
convKelv = kelvin - 273.15

print('-'*50)
print('Celsius ({}°C) para Fahrenheit é {}°F'.format(celsius1, convFanr),'\n','-'*50)
print('Fahrenheit ({}°F) para Celsius é {}°C'.format(fahrenheit, convCels1),'\n','-'*50)
print('Celsius ({}°C) para Kelvin é {}°K'.format(celsius2, convCels2),'\n','-'*50)
print('Temperatura absoluta em Kelvin ({}°K) para Celsius é {}°C'.format(kelvin, convKelv),'\n','-'*50)