# A função print()
'''
1- print()
    - É uma função q recebe um ou mais argumentos. Serve para imprimir o argumenta na tela de saida

2- sep=""
    - É um argumento NOMEADO (ou parametro) da função print, onde se seta a separação dos argumentos. 
    O sep por padrao é: sep=' '(espaço).

3- end=''
    - É um argumento NOMEADO utizado para mudar o final do print. O padão é uma quebra de linha, q tem 
    seus caracteres diferentes dependendo do sistema.

4- Quebra de linha
    - São os caracteres definidos para a quebra de linha. Sendo eles:
        - "\r\n" --> CRLF (sistema windows)
        - "\n" ----> LF (sistema MacOs)
    Onde o "\r" significa "RETURN" e o "\n" significa "LINE FEED"

Ex:
'''
# 1
print('argumento')

# 2
print(1,2,3,4,5)
print(1,2,3,4,5, sep='-') # definindo o serapador para "-" (traço)


# 3 e 4
print(1,2,3) # o end padrao sendo '\r\n' (quebra de linha)
print(1,2,3, end='FIM') # alterando o end para 'FIM' (uma string)