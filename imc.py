# CRIAR CALCULADORA IMC
from cs50 import get_float, get_string
from time import sleep
import os
name = get_string('\033[1;34;40mEnter your name:\033[0m ')
hight = get_float('\033[1;34;40mEnter your height:\033[0m ')
weight = get_float('\033[1;34;40mEnter your weight:\033[0m ')
imc = weight / ( hight * hight )
os.system(' cls ')
print('Olá {}'.format(name))
print('\033[1;31mCALCULANDO INFORMAÇÕES...\033[0m')
sleep(3)
print('Seu imc é:{:.2f}'.format(imc))
if imc <= 16.9:
    print('Você está muito abaixo do peso.')
elif imc > 17 and imc <= 18.4:
    print('Você está abaixo do peso.')
elif imc > 18.5 and imc <= 24.9:
    print('Seu peso está normal.')
elif imc > 25 and imc <= 29.9:
    print('Você está acima do peso.')
elif imc > 30 and imc <= 34.9:
    print('Obesodade grau I')
elif imc >= 30 and imc <= 40:
    print('Obesidade II')
else:
    print('Obesidade III')
