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


Envia uma notificação em caso de falha na execução.
Parâmetros:
nivel: Nível do alerta (1 - baixo, 2 - médio, 3 - alto).
base: Nome da base de dados envolvida na falha.
etapa: Etapa em que ocorreu a falha.


Coleta de Dados
1. Coleta de Dados dos Pokémons
Coleta dados dos Pokémons da PokéAPI e salva no banco de dados.
Dados de cada espécie de pokémon, são retirados da API "https://pokeapi.co/api/v2/pokemon", e categorizados em:
Name - Nome da espécie
Height - Altura do pokémon (importante 
Weight - Peso do pokémon (importante para moves como Low Kick e Grass Knot)
Type - O tipo de cada pokémon, podendo ter até dois
Base Experience - Parâmetro que influencia na taxa de crescimento do pokémon

2. Coleta de Dados de TMs
Coleta dados de TMs da PokéAPI e salva no banco de dados.
Dados de cada TM de versões diferentes do jogo, retirado da API "https://pokeapi.co/api/v2/machine", e categorizados em:
TM: Número da TM
Generation: Geração da franquia ao qual esta TM está listada
Move: Nome do movimento

3. Coleta de Dados de Movimentos
Coleta dados de Movimentos da PokéAPI e salva no banco de dados.
Dados de cada movimentos de pokémons, retirados da API "https://pokeapi.co/api/v2/move" e categorizados em:
Nome: Nome
Type: Tipo
Power: Poder base
Accuracy: Precisão
Power Points: PP (número de usos)
Effect: Pequena descrição do movimento e seus efeitos secundários.

Consulta das Tabelas no Banco de Dados
Consulta e exibe os nomes das tabelas presentes no banco de dados.

Conclusão
Este script fornece uma maneira automatizada de coletar, processar e armazenar dados da PokéAPI em um banco de dados SQLite,
além de monitorar e notificar possíveis falhas durante a execução.
