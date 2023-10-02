#ExerciciosPandas_001
#Usando a tabela ALUNOS. CSV; https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv

#Com base nisso, solucione os problemas propostos abaixo utilizando os conhecimentos adquiridos até aqui.

#1) Verifique se a base de dados possui dados nulos e, caso tenha, realize o tratamento desses dados nulos da forma que achar mais coerente com a situação.
#2) Os alunos "Alice" e "Carlos", não fazem mais parte da turma. Sendo assim, remova-os da base de dados.
#3) Aplique um filtro que selecione apenas os alunos que foram aprovados.
#4) Salve o DataFrame que possui apenas os alunos aprovados em um arquivo csv chamado "alunos_aprovados.csv".

#Extra: Ao conferir as notas dos alunos aprovados, notamos que algumas notas estavam incorretas. As alunas que tiraram nota 7.0, na verdade, tinham um ponto extra que não foi contabilizado. Sendo assim, substitua as notas 7.0 da base de dados por 8.0. 
#Dica: pesquise pelo método replace.

import pandas as pd
import numpy as np
#Importando a Tabela
url = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv" ,sep=",")
url
#1) Verifique se a base de dados possui dados nulos e, caso tenha, realize o tratamento desses dados nulos da forma que achar mais coerente com a situação.
pd.isna(url)
## Com este comando, é possível ver que há diversos registros constados como null
pd.isna(url).sum()
## Com o comando acima, conseguimos visualizar melhor, tendo a contagem de todos os resultados onde NaN aparece
nanzero = url.fillna(value= 0)
nanzero
## Criada a variavel nanzero, que executa o método fillNa (Que serve para preencher valores NA/NaN )
#2) Os alunos "Alice" e "Carlos", não fazem mais parte da turma. Sendo assim, remova-os da base de dados.
nanzero[["Nome"]]
###Usar o metodo QUERY para selecionar linhas especiicas
nomes_excluir = ['Carlos','Alice']
#Criamos o df Nomes_Excluir para usarmos como variavel
##Usamos o @ para conserguirmos passar a variavel na expressão
df_excluir = nanzero.query('@nomes_excluir in Nome')
df_excluir
# Aqui verificamos que a query foi bem sucedida
# Vamos então puxar agora somentes as que NÃO são Carlos e Alice
nanzero = nanzero.query('@nomes_excluir not in Nome')
nanzero
#3) Aplique um filtro que selecione apenas os alunos que foram aprovados.
Aprovadinhos = nanzero.query('Aprovado == True')
Reprovadinhos = nanzero.query('Aprovado == False')
Aprovadinhos
#Extra: Ao conferir as notas dos alunos aprovados, notamos que algumas notas estavam incorretas. As alunas que tiraram nota 7.0, na verdade, tinham um ponto extra que não foi contabilizado. Sendo assim, substitua as notas 7.0 da base de dados por 8.0. 
#Dica: pesquise pelo método replace.
Notas_a_corrigir = Aprovadinhos.query('Notas == 7.0')
Notas_a_corrigir = Notas_a_corrigir.replace([7.0],8.0)
#Usando Replace, trocamos o valor antigo [7.0] pelo novo 8.0. Poderiamos ter usado também o to_replace 7.0 com value 8.0
Notas_a_corrigir
#Agora vamos aplicar isso aos Aprovadinhos
Aprovadinhos = Aprovadinhos.replace(to_replace=7.0,value=8.0)
Aprovadinhos
#Com as notas dos Aprovadinhos corrigidas, vamos finalizar esse tratamento
#4) Salve o DataFrame que possui apenas os alunos aprovados em um arquivo csv chamado "alunos_aprovados.csv".
Aprovadinhos.to_csv('alunos_aprovados.csv')
