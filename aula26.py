# Formatção basica de strings
'''
A partir de agora, o metodo de formatação de str será focado no metodo "f str" q é o metodo mais moderno.
Mas, a maior parte pode ser aplicada as demais formas de formatação.
O metodo mais antigo de formatação de str é a interpolação. Então, alguns metodos de formatação do "f str" 
nao funcionam na interpolação.

1- referenciação de dados
    s --- string
    d --- int
    f --- float

2- números
    .<numero de digitos>f
    (caracter) > (quantidade) -- adiciona a esquerda caracateres ate forma a quantidade escolida
    +      --- ixibe numero positivos
    ,      --- separa o milhar por virgula
    =      --- força os numeros aparecerem apos o sinal de + ou -
    x ou X --- Hexadecimal

3- Padding
    (caracter)(><^)(quantidade)
    > --- a esquerda
    < --- a direita
    ^ --- ao centro

4 - Conversion flags
    r!
    s!
    a!
'''

# 1



# 2
print('2')
numero = 10000.78664874928
print(f'{numero:.2f}')
print( f'{222:0>10}' )
print( f'{numero:+}' )
print( f'{numero:,}' )
print( f'{222:0=+10}')
print( f'{-222:0=10}')
print(f'{numero:0=+10,.1f}') # tudo junto

print('2 - hexadecimal')
print(f' o hexadecimal de 15 é: {1500:x}')   # minúsculo
print(f' o hexadecimal de 15 é: {1500:X}')   # maiúsculo
print(f' o hexadecimal de 15 é: {1500:04X}') # com 4 casas
print(f' o hexadecimal de 15 é: {1500:08X}') # com 8 casas


# 3
print('3')

variavel = 'oi'
print(f'{variavel:->10}')
print(f'{variavel:-<10}')
print(f'{variavel:-^10}')


# 4
# não será visto agora. 
