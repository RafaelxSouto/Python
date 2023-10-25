from cs50 import get_string
from time import sleep
name = get_string('Seu nome: ')
print('LOADING...')
sleep(1.5)
print(f'Olá, {name}.')
print('-=-' * 20)
