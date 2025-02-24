# Exeercicio assistido
'''
Criar um algoritmo no qual ele cheka todas as letras de uma frase e retorna qual letra se repete mais
'''

FRASE = 'O python é uma linguagem de programação '\
    'Multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

str_edit = FRASE.replace(' ', '').replace('.', '')
tamanho_str = len(str_edit)
i = 0

mais_vezes = 0
letra_q_mais_apareceu = ''

while i < tamanho_str:
    letra_atual =  str_edit[i]
    vezes_q_s_repetiu = str_edit.count(letra_atual)

    if mais_vezes < vezes_q_s_repetiu:
        mais_vezes = vezes_q_s_repetiu
        letra_q_mais_apareceu = letra_atual
    
    i += 1
else:
    print(
        'A letra q mais se repete foi: '
        f'"{letra_q_mais_apareceu}" q se repetiu {mais_vezes} vezes'
    )