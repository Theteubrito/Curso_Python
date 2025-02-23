# Exercício sugeridopelo Gemini
'''
Crie um jogo onde o computador gera um número aleatório entre 1 e 100. O usuário tem que adivinhar o 
número. O programa deve dar dicas se o número digitado é maior ou menor que o número gerado. O jogo 
termina quando o usuário acertar o número.
'''

import random

numero_aleatorio = random.randint(1, 100)

texto1 = 'Jogo de Advihação'
texto2 = 'Um númumero entre 1 a 100 foi gerado, tente advinhar!'
texto3 = '(para sair no meio do jogo é so sugerir "S")'
print(f'{texto1:-^53}')
print(f'{texto2}')
print(f'{texto3:-^53}')



while True:
    print('-'*10)
    sugestao = input(" sugira um número -> ")

    try:
        if sugestao != 's':
            sugestao = int(sugestao)
        else:
            break
        
        if sugestao != numero_aleatorio:
            if sugestao < numero_aleatorio:
                print ('-' * 10)
                print(f"É maior que {sugestao}")
            
            else:
                print ('-' * 10)
                print(f"É menor que {sugestao}")
        else:
            print ('-' * 10)
            print('PARABÊNS!!!')
            print(f'Você acertou. O numero era {numero_aleatorio}')
            break
    except:
        print('Isso não é um numero válido')