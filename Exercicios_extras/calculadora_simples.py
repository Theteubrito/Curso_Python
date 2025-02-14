# Exercicio sugerido pelo Gmini
'''
Desenvolva um programa que simule uma calculadora. O usuario deve incerir dois números e a 
operação desejada (+,-,*,/). O programa deve realizar o cálculo e exibir o resultado.
'''

print('Calculadora simples')
print('               | + ..... Soma \n               | - ..... subtração\nOperadores:    | * ..... multiplicação\n               | / ..... divisão')

alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
operadores_validos = '+-*/'


n_1 = input('digite o primeiro númeor: ')

if n_1 not in alfabeto:
    n_2 = input('digite o segundo númeor: ')
    
    if n_2 not in alfabeto:
        operador = input('Qual a operação? ')
        if operador in operadores_validos:

            if operador == '+':
                soma = float(n_1) + float(n_2)
                print(f'{n_1}+{n_2}= {soma}')

            elif operador == '-':
                subtracao = float(n_1) - float(n_2)
                print(f'{n_1}-{n_2}= {subtracao}')

            elif operador == '*':
                multiplicacao = float(n_1) * float(n_2)
                print(f'{n_1}*{n_2}= {multiplicacao}')

            else:
                divisao = float(n_1) / float(n_2)
                print(f'{n_1}/{n_2}= {divisao}')
            
        else:
            print('vc nao digitou um operador valido!')

    else:
        print('vc digitou uma letra')

else:
    print('vc digitou uma letra')