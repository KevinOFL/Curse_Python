#Desafio calcúlo de IMC

print('=-'*36)
print(' '*27,'\033[7mCalcúlo de IMC\033[m')
print('=-'*36)

peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura atual: '))

imc = peso / (altura * altura)

print('=-'*36)

if imc < 18.5:
    print('''IMC {:.2f}
    \033[36;1mAbaixo do peso\033[m'''.format(imc))
elif imc >= 18.5 and imc < 25:
    print('''IMC {:.2f}
        \033[32;1mPeso ideal\033[m'''.format(imc))
elif imc >= 25 and imc < 30:
    print('''IMC {:.2f}
        \033[33;1mSobrepeso\033[m'''.format(imc))
elif imc >= 30 and imc < 40:
    print('''IMC {:.2f}
        \033[31;1mObesidade\033[m'''.format(imc))
elif imc > 40:
    print('''IMC {:.2f}
        \033[7mObesidade mórbida\033[m'''.format(imc))

print('=-'*36)
