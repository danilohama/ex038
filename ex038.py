"""Escreva um programa que leia dois números inteiros e compare-os mostrando uma mensagem na tela:
> O Primeiro valor é MAIOR
> o Segundo valor é MAIOR
> Não existe valor maior, os dois são iguais
"""
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('O primeiro valor é \33[0:32mMAIOR\33[m')
elif num1 == num2:
    print('\33[0:31mOs dois valores são exatamente iguais!')
else:
    print('O segundo valor é \33[0:32mMAIOR\33[0m')
