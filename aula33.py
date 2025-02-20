# Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string
"""
1- Built-in
     Refere-se a funções e modulos q ja vem integrada na python, as funções padão. Elas estao disponiveis 
     para uso sem a necessidade de intalar pacotes adicionais. Qualguns exemples de funções built-in:
     - print()
     - len()
     - type()

2- Documentação
    A documentação é o manual da linguagem, nela vem discrito tudo. É uma pratica importante a leitura 
    da mesma.
    https://docs.python.org/pt-br/3/library/stdtypes.html

3- Tipos imutaveis
    Tipos imutaveis nao dados q nao podem ser DE FATO alterados, editados. pra se mudar um dado imutavel 
    é preciso criar outro.
    dados imutaveis q ja vimos:
    - str
    - int
    - floar
    - bool

ex:
"""
# 3

str = 'Matheus'
print (id(str))
# pra se alterar esta variavel é preciso criar outra e sobreescrever a anterior
str = 'Siqueira'
print (id(str))