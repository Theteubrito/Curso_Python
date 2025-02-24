# introdução ao for/ in (Condicionais para laços de repetição finitos)
'''
Ate aqui usamos o while para iterações de string. Porem, o while é usado pra laços realmente infinitos ou 
para laços de repetiçoes indefinidos(imprevizíveis). Como por explempro, oprojeto extracurricular q eu fiz 
para advinhar um numero aleatorio gerado pelo programa (jogo_do_advinha.py).
Para iterações de string, q sao previziveis e finitas (afinal o fim do laço é vizivel) se usa, de 
fato, o For.

Ex:
'''
TEXTO = 'Python'

# iteração com while
print('-'*10)

tamanha_texto = len(TEXTO)
indici = 0
while indici < tamanha_texto:
    print(TEXTO[indici])
    indici += 1

print('-'*10)



# iteração com for
print('-'*10)

for letra in TEXTO:
    print(letra)

print('-'*10)
