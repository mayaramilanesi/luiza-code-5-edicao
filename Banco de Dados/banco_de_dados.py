'''
SGBD - SOFTWARE QUE AJUDA NA MANIPULAÇÃO DA BASE DE DADOS - mongoDB, MySQL
SLI - linha de comandos
DBA - GERENCIADOR DO BANCO DE DADOS

BANCOS DE DADOS RELACIONAIS - TABELAS COM LINHAS E COLUNAS


#### COMANDOS ######

-> DDL - Responsável por alterar itens na tabela

- CREATE - cria tabela
- DROP - deleta tabela
- ALTER - alterando
- TRUNCATE - limpar todos os dados da tabela
- RENAME - renomear tabela


-> DQL - MANIPULAÇÃO DOS DADOS

- SELECT


-> DML - MANIPULANDO DADOS

- INSERT - inserindo dados
- UPDATE - atualizando dados
- DELETE - deletando dados
- LOCK - 
- CALL - 
- EXPLAIN PLAN - 


-> DCL - DBA é responsável - devine as regras e permissões de cada usuário

- GRANT
- REVOKE


-> TCL - COMANDOS DE TRANSAÇÃO DE DADOS

- COMMIT
- ROLLBACK
- SAVE POINT



-> CONSTRAINS - REGRAS PARA TRABALHAR COM AS TABELAS

- PRIMARY KEY - restrição que identifica EXCLUSIVAMENTE cada registro em uma tabela, devem ter valores únicos e não pdoem ter valores null
- DEFAULT - é utilizado para inserirmos um valor padrão em uma coluna. É inserido automaticamente nos registros se nenhum valor for especificado
- NOT NULL - garante que uma coluna não admita valores null - obriga o preenchimento do campo em questão
- UNIQUE - impede que valores duplicados sejam inseridos na coluna



-> FOREIGN KEY
- Evita ações que destruam links entre tabelas, se refere a PRIMARY KEY em outra tabela. A tabela com foreign key é tabela filha e a primary key é tabela mãe



- CREATE TABLE - Cria uma tabela
- DROP TABLE - Exclui uma tabela
- ALTER TABLE - Adiciona, exclui ou modifica colunas em uma tabela existente
- INSERT INTO - insere novos registros em uma tabela
- UPDATE - modifica os registros de uma tabela, DEVE SEMPRE USAR WHERE JUNTO
- DELETE - exclui os registros de uma tabela, DEVE SEMPRE USAR WHERE JUNTO
- SELECT - seleciona dados de um banco de dados
- SQL JOINS - verificar foto
- WHERE - usada para filtrar registros
- ORDER BY - classifica o conjunto em ordem crescente ou decrescente
- GROUP BY - agrupa as linhas que tem os mesmos valores em linhas de resumo, é usada juntamente com COUNT, MAX, MIN, SUM, AVG
- LIKE - é usado em uma cláusula WHERE para procurar um padrão especificado em uma coluna.



- no mongo, para criar o objectid automaticamente, basta não inserir o _id no início de cada coleção


-> Agregações

- pROCESSAM VÁRIOS DOCUMENTOS E  RETORNAM OS RESULTADOS CALCULADOS. pODEMOS AGRUPAR VALORESde vários documentos juntos, executar operações nos dados agrupados para retornar um único resultado e analisar as mudanças de dados ao longo do tempo
'''