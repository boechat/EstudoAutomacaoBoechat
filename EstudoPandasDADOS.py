#OBJETIVOS
##1 explorar características gerais de uma base de dados
##2 realizar análises exploratórias com diferentes métodos
##3 lidar com valores nulos
##4 remover registros inconsistentes
##5 aplicar filtros
##6 criar diferentes colunas

#TAREFAS DO TRELLO
## IMPORTAR E CONHECER A BASE DE DADOS
## ANALISE EXPLORATORIA DOS DADOS
## TRATAR VALORES NULOS
## REMOVER REGISTROS INCONSISTENTES
## APLICAR FILTROS
## SALVAR OS DADOS
##
## CRIAR COLUNAS NUMÉRICAS
## CRIAR COLUNAS CATEGORICAS

import pandas as pd
import numpy as np

##Lê a tabela usando csv, usando a separação de PONTO E VIRGULA
#tabela = pd.read_csv("aluguel2.csv",sep=";")
#print(tabela)

##Lê a tabela usando url, usando a separação de PONTO E VIRGULA
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
tabela = pd.read_csv(url,sep=';')
##pega apenas os cinco primeiros dados
#tabela = tabela.head(15)
#tabela = tabela.describe()

##Url da tabela de alunos
# alunos = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv', sep=';')

## Tira todas as instancias de  ROWS com NaN valores
# tabela.dropna()

##Quantidade de Linhas x Colunas
#tabela = tabela.shape

##Nomes das Colunas
#tabela = tabela.columns

##Infos dos dados, retornando inclusive quantidade de dados Não-Nulos e o DTYPE!
#tabela = tabela.info()
##Para pegar uma info especifica, usar [] ou [[]]
#tabela = tabela['Quartos']
#tabela = tabela[['Quartos','Valor']]


##Troca todas as instancias de NaN para o valor 0
#tabela=tabela.replace(np.nan,0)

##QUAL O VALOR MEDIO POR TIPO DE IMOVEL?
##Usar metodo mean() para tirar a média. Selecionando uma coluna especifica de valor
#tabela = tabela['Valor'].mean()
##Agora agrupando por tipo de imovel
#tabela = tabela.groupby('Tipo')
##E agora pegando a média. Precisa especificar que apenas as colunas numericas serão lidas para não haver erros!
#tabela = tabela.groupby('Tipo').mean(numeric_only=True)
##Melhorando a visualização, selecionando apenas aa coluna valor, agrupando por TIPO
#tabela.groupby('Tipo')['Valor'].mean()
##Transformando a visualização em Dataframe, passamos a coluna 'Valor' em [[ ]]
#tabela.groupby('Tipo')[['Valor']].mean()
##Classificando os valores do maior ao menos
#tabela.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

##Criando um Gráfico
#df_preco_tipo = tabela.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
##Colocando o plot##
#df_preco_tipo.plot(kind='barh', figsize=(14, 10), color ='purple');

##Criando um DataFrame manualmente
#df = pd.DataFrame({
#   'Animal': ['Cachorro', 'Gato', 'Elefante', 'Cachorro', 'Gato', 'Elefante'],
#   'Cor': ['Preto', 'Branco', 'Cinza', 'Marrom', 'Preto', 'Marrom'],
#   'Quantidade': [2, 3, 1, 4, 2, 2]
# })

##Buscando todos os valores unicos em uma coluna especifica
#tabela = tabela.Tipo.unique()

##Criando os tipos de Imoveis Comerciais e jogando numa variavel
imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

##Usar o metodo QUERY para selecionar linhas especiicas, pegando todas as linhas do dataframe em que o tipo do imovel seja um dos presentes em imoveis_comerciais
##Usamos o @ para conserguirmos passar a variavel na expressão
#tabela = tabela.query('@imoveis_comerciais in Tipo')
##Agora, puxando todos que não são do tipo
#tabela = tabela.query('@imoveis_comerciais not in Tipo')
##Selecione apenas os imóveis que possuem uma ou mais suítes.
#tabela.query('Suites >= 1')


##QUAL O PERCENTUAL DE CADA TIPO DE IMOVEL NA BASE DE DADOS?

##Faz a contagem de quantos tem na coluna Tipos
#tabela = tabela.Tipo.value_counts()
##Como a nossa pergunta é qual o percentual de cada tipo de imóvel, precisamos visualizar essas quantidades em percentuais. Isso é simples! Basta acrescentar um parâmetro no value_counts() chamado normalize=True.
#tabela = tabela.Tipo.value_counts(normalize=true)
##Para melhorarmos essa visualização, vamos realizar o mesmo processo que fizemos anteriormente para transformar o series em dataframe.
#tabela = tabela.Tipo.value_counts(normalize=True).to_frame()

## salvando o dataframe em uma variável
#df_exemplo = df['Tipo'].value_counts(normalize=True).to_frame().sort_values('Tipo')
## alterando o nome da coluna "Tipo" para "Percentuais"
#df_exemplo.rename(columns={'Tipo': 'Percentuais'}, inplace=True)
## visualizando o dataframe
#df_exemplo

###TRATANDO DADOS NULOS

##Visualizando todos os dados NULL (TRUE) e NAO NULOS (FALSE)
#tabela = tabela.isnull()
##Visualizando como somatório
#tabela = tabela.isnull().sum()
##Substituindo os valores nulos por zero (0)
tabela = tabela.fillna(0)
##OUTRAS FORMAS DE RESOLUÇÃO
##Removendo usando dropna() ->  remove todas as linhas ou colunas que possuem pelo menos um valor nulo.
##Preenchendo com fillna() -> também pode usar o metodo o method=”ffill” ou method=”bfill” para preencher os valores nulos com o valor anterior ou posterior, respectivamente.
##Interporlar com interpolate() -> preencher os valores nulos com valores calculados a partir dos valores vizinhos.

##REMOVENDO REGISTROS

## Remover valores inconsistentes, tais como: partamentos que possuem valor de aluguel igual a 0   E   apartamentos com o valor do condomínio igual a 0.
#tabela= tabela.query('Valor == 0 | Condominio == 0')
##Pegar os indices que  possuem o valor 0. guardando em uma variavel chamada REGISTROS_A_REMOVER
registros_a_remover = tabela.query('Valor == 0 | Condominio == 0').index
#Feito isso, iremos dar drop na TABELA usando a REGISTROS_A_REMOVER, usando o parametro axis = 0 (Remover linhas, se fosse axis = 1 removia colunas)
#Usaremos o parametro 'inplace' como true, para que não seja preciso atribuir(tabela = )
tabela.drop(registros_a_remover, axis=0, inplace=True)

#Agora vamos remover a coluna TIPO, pois o unico valor que contem nela é Apartamento, então é redundante.
tabela.drop('Tipo', axis=1, inplace=True)


#APLICANDO FILTROS
#Filtrar por Apartamentos que possuam 1 quarto e aluguel menor que R$ 1200;
#Filtrar por Apartamentos que possuam pelo menos 2 quartos, aluguel menor que R$ 3000 e área maior que 70 metros quadrados.

##Filtrar por Apartamentos que possuam 1 quarto e aluguel menor que R$ 1200;
#O primeiro passo é selecionar os apartamentos com um quarto.
# Para isso, vamos pegar a variável que está com o dataframe, 'tabela', e selecionar a coluna Quartos, que é de nosso interesse. Fora dos colchetes, adicionaremos "igual igual a 1".
tabela['Quartos'] == 1
#Como retorno, recebemos uma series de valores booleanos: As linhas com "True" são as que a coluna "Quartos" possui valor 1. As linhas com valor "False" são as que a coluna "Quartos possui valor diferente de 1.
#Criando a variavel para receber esses valores selecao1
selecao1 = tabela['Quartos'] == 1
#O dataframe Pandas tem a propriedade de receber uma series booleana: as linhas com valor "True" são consideradas e as com valor "False" não são lidas.
tabela[selecao1].head(5)
#Agora, faremos outra seleção, pegando o valor menor que 1200
tabela['Valor'] < 1200
#Passando pra variavel
selecao2 = tabela['Valor'] < 1200
tabela[selecao2].head(5)
#Para obter os dois cenários juntos, 1 quarto e aluguel menor que R$ 1200, precisamos é necessário juntar as duas seleções e aplicá-las ao nosso dataframe.
selecao_final = (selecao1) & (selecao2)
tabela[selecao_final].head()
print(tabela[selecao_final].head())
#Agora podemos salvar essa seleção no dataframe em outra variável que será de fácil acesso, tabela1
tabela1 = tabela[selecao_final]

##Filtro 2: Apartamentos com 2 quartos, aluguel < R$ 3000 e área > 70 metros quadrados
#Desta vez, ao invés de fazer seleções separadas e salvar em variáveis distintas. O código é:
selecao = (tabela['Quartos'] >= 2) & (tabela['Valor'] < 3000) & (tabela['Area'] > 70)
#Criamos uma variável chamada selecao e nela realizamos as três seleções solicitadas. A primeira é para quando a coluna "Quartos" tiver um valor maior ou igual a 2.
#Utilizamos o operador and para uni-la à próxima seleção: quando o valor do aluguel for menor que 3 mil.
#Em seguida, utilizamos outra vez o operador and para unir a terceira e última seleção às demais, quando a área do apartamento é maior que 70.
# Na próxima linha, passaremos a seleção ao nosso dataframe.
tabela[selecao]
#Obtivemos o dataframe resultante do filtro que criamos. Vamos salvar tabela[selecao] em outra variável, caso seja necessário utilizá-la depois.
tabela2 = tabela[selecao]

##SALVANDO OS DADOS
## Como lemos esse arquivo no formato CSV, é recomendável que agora, no momento de salvar, ele seja salvo neste mesmo formato.
## Para isso, utilizaremos um método do Pandas chamado to_csv().
# tabela.to_csv('dados_apartamentos.csv')
# tabela.read_csv('dados_apartamentos.csv')
## O retorno é um dataframe completo, com algo diferente dos anteriores: a coluna "Unnamed: 0". Para nao retornar essa coluna, passaremos INDEX = FALSE
# tabela.to_csv('dados_apartamentos.csv', index=False)
## Lembrando que, quando usamos o to_csv() para salvar um arquivo em formato CSV, automaticamente ele é salvo separado por vírgulas (que é o padrão do CSV).
## No entanto, quando realizamos a leitura da nossa base de dados, notamos que ela estava separada por "ponto e vírgula (;)".
## Sendo assim, quando salvarmos a nova versão da nossa base de dados, é recomendável manter esse padrão e salvá-la em CSV, separada por ponto e vírgula. Vamos fazer isso!
# tabela.to_csv('dados_apartamentos.csv', index=False, sep=';')
# pd.read_csv('dados_apartamentos.csv', sep=';')

##SALVANDO OS OUTROS DADOS EM CSV
#tabela1.to_csv('filtro_1.csv', index=False, sep=";")
#tabela2.to_csv('filtro_2.csv', index=False, sep=";")

### CRIAR COLUNAS NUMÉRICAS
## A primeira coluna a ser criada é "valor_por_mes", onde colocaremos um compilado dos gatos mensais de cada imóvel, incluindo aluguel e condomínio.
## A segunda coluna é "valor_por ano" e corresponde aos gastos anuais por imóvel, ou seja, IPTU mais 12 meses de aluguel e condomínio.

urlcriar = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(urlcriar, sep=';')
## Para isso, chamamos o dataframe como se fôssemos escolher uma coluna existente, porém, passamos o nome da coluna que será criada (VALOR_POR_MES):
## Neste caso, podemos considerar o valor do aluguel e o valor do condomínio, que estão, respectivamente, nas colunas "Valor" e "Condomínio". Sendo assim, basta somá-las.
#dados['Valor_por_mes'] = dados['Valor'] + dados['Condomínio']
## Nas linhas com valores NaN, não será feito o calculo, então é preciso transformar esses dados em 0
#dados.fillna(0,inplace = True)
#dados['Valor_por_mes'] = dados['Valor'] + dados['Condomínio']
##Agora, criaremos "Valor_por_ano" seguindo um procedimento semelhante. Para esta coluna, devemos considerar os gastos mensais multiplicados por 12 (meses do ano) somado ao valor do IPTU.
#dados['Valor_por_ano'] = dados['Valor_por_mes'] * 12 + dados['IPTU']

### CRIAR COLUNAS CATEGORICAS
## A primeira coluna será chamada de "Descrição" e deve conter uma sumarização das principais informações de cada um dos imóveis da nossa base de dados.
## Entre elas é necessário constar o tipo de imóvel, o bairro, a quantidade de quartos e de vagas de garagem.
## A segunda coluna se chamará "Possui_suite" e será binária, onde devemos informar se o imóvel tem suíte ou não.
#dados['Descricao'] = dados['Tipo'] + dados['Bairro']

## As informações ficaram grudadas, sem nenhum espaço, então podemos personalizar acrescentando o termo "em", com espaço antes e depois, entre o tipo e o bairro:
#dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro']
##Agora que entendemos como funciona, incluir as outras informações:
#dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
#                                        dados['Quartos'] + ' quarto(s) ' + \
#                                        ' e ' + dados['Vagas'] + ' vaga(s) de garagem.'

## Perceba que estamos utilizando barra invertida \ para quebrar linha e facilitar a visualização do comando.
## Ao executar, note que temos um TypeError, porque não é possível concatenar strings com números inteiros, que é o caso das colunas numéricas de quartos e vagas.
## Sendo assim, é necessário converter essas informações para string usando o método .asType() e informando para qual tipo será feita a conversão.
dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
                                        dados['Quartos'].astype(str) + ' quarto(s) ' + \
                                        ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem.'
print(dados.head())

##COLUNA BINÁRIA
## precisamos analisar a coluna já existente que possui a quantidade de suítes em cada um dos imóveis.
## Sendo assim, teremos que analisar cada linha dessa coluna e colocar "Sim" para as que tiverem valor maior que zero, e "Não" para o caso contrário.
## lambda = funções personalizadas que podem ser feitas em uma linha de codigo)
dados['Possui_suite'] = dados['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")
## usamos o método .apply(), utilizado para aplicar uma determinada função em um conjunto específico de dados.
## No nosso caso, esse conjunto é a coluna "Suites", e a função, é do tipo lambda - funções personalizadas que podem ser escritas em uma única linha.
## Nesta função, x equivale a cada linha da coluna de suítes. Então, fizemos uma condicional if em que se o valor de x, ou seja, o registro da linha, for maior que zero, deve ser colocado "Sim", caso contrário (else), coloca-se "Não".
## Nós a salvaremos no formato CSV e a chamaremos de "dados_completos_dev.csv", passando alguns parâmetros, como index e sep:
# dados.to_csv('dados_completos_dev.csv', index=False, sep=';')

### OUTRAS FORMAS DE CRIAR COLUNAS
## Atribuição direta de valores a uma nova coluna:
#import pandas as pd
#df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
#df['C'] = [7, 8, 9]
#df

### Criação de uma coluna a partir de operações entre outras colunas:
#import pandas as pd
#df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
#df['C'] = df['A'] + df['B']
#df

### Utilização do método assign() para criar uma nova coluna:
#import pandas as pd
#df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
#df = df.assign(C=[7, 8, 9])
#df

### Utilização do método apply() para aplicar uma função a uma coluna existente e criar uma nova coluna:
#import pandas as pd
#df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
#df['C'] = df['A'].apply(lambda x: x * 2)
#df



#print(tabela)


#print(imoveis_comerciais)
#print(registros_a_remover)



