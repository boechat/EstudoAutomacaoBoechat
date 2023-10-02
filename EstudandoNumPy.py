# Esta biblioteca é voltada para computação numérica e científica, portanto, trabalharemos com objetos do tipo array que servem para realizar operações matemáticas e estatísticas, muito importantes em ciência de dados.

# Trabalharemos com um dataset de preços de maçãs.
# Ou seja, uma tabela de dados semelhante ao que vemos em softwares como Excel e Google Planilhas.
# A ideia é que comecemos a analisar esses dados seguindo os mesmo processos utilizados nos softwares citados, como, por exemplo, somar os valores de uma coluna, calcular a média ou realizar operações entre diferentes colunas.
# Para isso, usaremos a ferramenta NumPy, que é uma biblioteca Python.

import numpy as np
import pandas as pd
#url -> apples_ts.csv
dado = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'
df = pd.read_csv(dado)
#print(df)

## Na célula seguinte, chamaremos a função .loadtxt() passando o nome do arquivo 'apples_ts.csv'.
## Precisamos passar, também, o delimitador do arquivo que, por ser CSV, tem como padrão ser delimitado por vírgula delimiter=','.

## note que, na primeira coluna, temos textos correspondentes aos nomes das cidades. Sendo assim, precisamos solicitar todas as colunas, com exceção desta, de índice zero.

#teste = np.loadtxt(dado,delimiter=',')
#print(teste)

## Ao executarmos, é retornado um erro, informando que não foi possível converter uma string em um float.
## Isso acontece porque, quando trabalhamos com arrays em NumPy, precisamos que exista somente um único tipo de dado dentro do array.

## Para este array, usaremos a função np.arange() que deve gerar a sequência de valores.

## Ao executarmos esta célula, nos é retornado um array com a lista de contagem do número 1 ao 87, o que significa que conseguimos gerar essa sequência de 1 em 1.
## Sendo assim, podemos passar esta função para usecols, que está no comando da célula anterior:

teste = np.loadtxt(dado, delimiter=',', usecols=np.arange(1, 88, 1))
#print(teste)

###CONSIDERANDO O PROBLEMA ABAIXO:
##crie um array, utilizando a função np.arange(), que liste todos os anos nos quais aconteceram ou estão previstos de acontecer a Copa do Mundo,
## considerando o intervalo fechado dos anos de 2000 a 2102.
###RESULTADO:
#import numpy as np
#ano_inicial = 2002
#ano_final = 2102
#np.arange(ano_inicial, ano_final + 1, 4)

###TRANSFORMANDO UMA LISTA EM UM ARRAY NUMPY:
#import numpy as np
## cria uma lista
#lista = [1, 2, 3, 4, 5]
## transforma a lista em um array Numpy
#array = np.array(lista)
#print("Lista: ", lista)
#print("Array: ", array)


##Usaremos agora a função ndim, que verifica a quantidade de dimensões do array. Ao executarmos o comando a seguir:
dado.ndim
##Obtemos 2 como retorno. Este valor refere-se à quantidade de informações pelas quais nossos dados estão variando.
## Em nosso caso, temos um dado tabelado 2D, 2 dimensões, linhas e colunas.

## Outra informação que podemos obter é a quantidade de elementos de um array. Para isso, utilizamos o comando:
dado.size
##Como retorno, obtemos 522.
##Além disso, usaremos shape para verificar o número de elementos em cada dimensão:
dado.shape
##Como retorno temos (6, 87), o que significa que temos 6 linhas e 87 colunas em nosso dataset.
##Mas, como já dito, podemos inverter a estrutura dos nossos dados trocando as linhas por colunas. Para isso, utilizamos o método da transposição, T:
dado.T
##Feito isso, nos é retornado um array semelhante a este:
##array([[ 1.2013, 79.72, 42.67, 62.55, 48.26, 71.25 ], [ 2.2013, 81.08, 44.37, 62.73, 51.01, 71.35 ], [ 3.2013, 79.68, 44.73, 63.43, 50.91, 70.9 ], [ 4.2013, 79.8, 46.75, 63.83, 53.94, 71,92 ], [5.2013, 80.63, nan, 66.06, 61.27, 72.91 ], ...

##E agora, guardando a info de dado.T
dados_transposto = dado.T

## criaremos um array chamado datas para armazenar uma coluna específica do array dado_transposto.
##, chamamos nosso array e entre colchete usamos : entre dois números para informar um intervalo, mas, neste caso, queremos pegar todas as linhas do dataset, por isso o utilizamos sozinho.
## passamos a coluna em questão. Por ser a primeira, corresponde à posição 0.
datas = dados_transposto[:,0]
## podemos separar as informações referente aos preços. Vamos armazená-las em uma variável chamada precos. Temos 5 localidades, que correspondem às 5 colunas, então nosso intervalo vai de 1 a 6.
precos = dado_transposto[:,1:6]

### Criando visuais para os dados
## Para isso, importaremos a biblioteca Matplotlib e a apelidaremos de plt:
import matplotlib.pyplot as plt
## Em seguida, usaremos a função plot() passando a informação que queremos nos eixos x e y,

plt.plot(datas,precos[:,0])
