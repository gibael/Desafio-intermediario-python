"""Explicação:

'T' é o número de casos de teste.
O loop for itera sobre cada caso de teste.
'N' e 'K' são lidos usando 'map(int, input().split())' para converter os valores de entrada em inteiros.
O número de garrafas no segundo dia é calculado usando a fórmula '(N // K) + (N % K)', onde // representa a divisão inteira e % representa o operador de módulo.
O resultado é impresso para cada caso de teste."""

# "T" é o número de casos de teste.
T = int(input())

# O loop "for" itera sobre cada caso de teste.
for i in range(T):
    N, K = map(int, input().split()) #"N" e "K" são lidos usando "map(int, input().split())" para converter os valores de entrada em inteiros.
    
    segundo_dia = (N // K) + (N % K) #O número de garrafas no segundo dia é calculado usando a fórmula "(N // K) + (N % K)", onde "//" representa a divisão inteira e "%" representa o operador de módulo.
    
    print(segundo_dia)