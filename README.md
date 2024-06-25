Bem vindo a Pokedex de batalha.

Aqui, com o intuito de montar um time competitivo de batalha, para qualquer geração da franquia,
apresento uma ferramenta de busca tanto de pokémons, quanto de movimentos e TMs.

Documentação do Código
Descrição
Este script coleta dados de três diferentes endpoints da API do Pokémon (PokéAPI), armazena esses dados em um banco de dados SQLite,
realiza algumas manipulações básicas nos dados e envia notificações em caso de falhas. O script é dividido em três partes principais:

Coleta de dados de Pokémons.
Coleta de dados de TMs.
Coleta de dados de Movimentos.

Além disso, o script possui funções auxiliares para salvar dados no banco de dados e enviar notificações.

Dependências
Este script depende das seguintes bibliotecas:
pandas
requests
sqlite3
plyer
datetime

Estrutura do Código
Funções Auxiliares
save_to_db(df, table_name, conn)
Salva um DataFrame em uma tabela no banco de dados SQLite.

Parâmetros:
df: DataFrame a ser salvo.
table_name: Nome da tabela no banco de dados.
conn: Conexão com o banco de dados SQLite.


Envia uma notificação em caso de falha na execução.
Parâmetros:
nivel: Nível do alerta (1 - baixo, 2 - médio, 3 - alto).
base: Nome da base de dados envolvida na falha.
etapa: Etapa em que ocorreu a falha.


Coleta de Dados
1. Coleta de Dados dos Pokémons
Coleta dados dos Pokémons da PokéAPI e salva no banco de dados.

2. Coleta de Dados de TMs
Coleta dados de TMs da PokéAPI e salva no banco de dados.

3. Coleta de Dados de Movimentos
Coleta dados de Movimentos da PokéAPI e salva no banco de dados.

Consulta das Tabelas no Banco de Dados
Consulta e exibe os nomes das tabelas presentes no banco de dados.

Conclusão
Este script fornece uma maneira automatizada de coletar, processar e armazenar dados da PokéAPI em um banco de dados SQLite,
além de monitorar e notificar possíveis falhas durante a execução.
