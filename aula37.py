# Pulando algumas repetições
'''
Continue
    Enquanto o "break" mata a repetição, o continue PULA os demais comandos do laço diretamente 
    de volta ao while

Ex:
'''

#
contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6:
        print('nao vou mostrar o 6')
        continue

    if contador >=10 and contador <=30:
        print('.')
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou!')