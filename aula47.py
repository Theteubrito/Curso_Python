# exercicio
'''
Jogo da forca
Faça um jogo para o ususario advinar qual a palavra sereta.
- vc vai propor uma palavra secreta qualquer e vai dar a possibilidade parao usuario  digitar apenas 
uma letra.
- quando o usuário digitar uma letra , voce vai conerir se a letra digitada está na palavra secreta.
    - se a letra estiver na palavra secreta; exiba a letra;
    - se a letra digitada nao estiver na palavra; exiba "*".
- faça contagem de tentativas do seu usuario.
'''
import os # permite usar comandos de cmd

SEGREDO = 'gato'
acerto = ''

tentativas = 0

print(' ______________________________ ')
print('|--------Jogo do segredo-------|')
print('|Tente acerta a palavra secreta|')
print('|______________________________|')
while True:
    print('|                              |')
    sugestao = input('|------Sugira uma letra ->  ').lower()
    tentativas += 1

    if len(sugestao) > 1:
        print('|                              |')
        print('|   Digite uma letra por vez   |')
        continue

    if sugestao in SEGREDO:
        acerto += sugestao

    palavra_formada = ''
    for letra in SEGREDO:
        if letra in acerto:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    if palavra_formada != SEGREDO:
        print('|______________________________|')
        print('|                              |')
        print(f'|-           -{palavra_formada}-           -|')
        print('|______________________________|')

    else:
        os.system("cls") # comando de limpar tudo no cmd
        print(' ______________________________ ')
        print('|                              |')
        print('|------PARABENS VC ACERTOU-----|')
        print('|                              |')
        print(f'|------A palavra era: {SEGREDO} ----|')
        print('|                              |')
        print(f' ---Número de tentativas: {tentativas} ---')
        print('|______________________________|')
        break
    