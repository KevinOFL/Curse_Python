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
print('Celsius ({:.2f}°C) para Fahrenheit é {:.2f}°F'.format(celsius1, convFanr),'\n','-'*50)
print('Fahrenheit ({:.2f}°F) para Celsius é {:.2f}°C'.format(fahrenheit, convCels1),'\n','-'*50)
print('Celsius ({:.2f}°C) para Kelvin é {:.2f}°K'.format(celsius2, convCels2),'\n','-'*50)
print('Temperatura absoluta em Kelvin ({:.2f}°K) para Celsius é {:.2f}°C'.format(kelvin, convKelv),'\n','-'*50)