# como o for funciona por baixo dos panos e mais alguns conseitos
'''
- Métodos
    Funções dentro de objetos: Métodos são funções que pertencem a uma classe e operam nos 
    dados (atributos) dessa classe. São ações aplaicadas a um objeto.
    Ex:
        str = "'olá mundo'.lower()
"
- Iteraveis
    É um elemnto capaz de retornar seus membos, um por vez( como se fosse uma lista). Este elemento 
    possui um metodo chamado iterador.
    Ex:
        str
        tupla
        lista
        dicionário

- iterador
     E o metodo q entrega os elementos de uma interavel

- iter
     É um iterador.
     Exs:
        str = 'olá mundo'.__iter__()
        str = iter('olá mundo')

- Next
    É um método especial que faz parte do protocolo de iteração. Ele é fundamental para entender como 
    os loops "for" e outras formas de iteração funcionam.
    O método ".__next__()" é responsável por retornar o próximo elemento de uma sequência.
    Ex:
        str = 'olá mundo'.__next__()
        str = next('olá mundo')

- fluxo do for
    Dito tudo isso, vamos entender o fluxo do for

Ex:
'''
# for                   letra                      in   texto   :
#  |                      |                         |     |
# for (try: next(interador = iteravel) execpt...:) in (iteravel):

iteravel = 'Python'
iterador = iter(iteravel)
while True:
    try:
        print(next(iterador))
    except StopIteration:
        break