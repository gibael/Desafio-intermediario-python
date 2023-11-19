

"""
#Desafio
Daenerys é a khaleesi dos Dothraki. Juntamente com Drogon, eles vão atrás do Tyrion, 
para tentar dominar Westeros. Ela possui, além do seu dragãozinho, um rastreador que mede o nível de energia de qualquer ser vivo. 
Todos os seres com o nível menor ou igual a 8000, ela considera como se fosse um inseto. Quando passa deste valor, que foi o caso do Drogon,
ela se espanta e grita “Mais de 8000”. Baseado nisso, utilize a mesma tecnologia e analise o nível de energia dos seres vivos.

Entrada
A primeira linha contém um número inteiro C relativo ao número de casos de teste. Em seguida, haverá C linhas, 
com um número inteiro N (100 <= N <= 100000) relativo ao nível de energia de um ser vivo.

Saída
Para cada valor lido, imprima o texto correspondente.

 
Exemplo de Entrada	Exemplo de Saída
3                   Mais de 8000!
8001                Inseto!
100                 Inseto!
200
"""

# definindo uma função. Esta função recebe um argumento nivel
def analisar_nivel_energia(nivel):
    if nivel > 8000:
        return "Mais de 8000!"
    else:
        return "Inseto!"

# Número de casos de teste
C = int(input())

# Loop para cada caso de teste
for i in range(C):
    # Nível de energia do ser vivo
    N = int(input())

    # Analisa e imprime o resultado
    resultado = analisar_nivel_energia(N)
    print(resultado)