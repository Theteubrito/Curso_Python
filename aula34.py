# repetição part1
'''
1- while -- Enquanto
    Execulta uma ação enquato a condição for verdadeira.
    
    ATENÇÃO!!!
    o uso do wile em um codigo no qual sua CONDIÇÃO DE FINALIZAÇÃO NÃO ESTA BEM DEFINI DA pode cair 
    em um estado chamado "loop infinito" E PODE TRAVAR A MAQUINA (COMPUTADO).
    Ex:
        while:
            print('1')

2 break -- quebrar
    Usado para quebrar uma repetição.
    Ex:
        while:
            print('1')
        break

Ex:
'''
condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break
print('Acabou!')