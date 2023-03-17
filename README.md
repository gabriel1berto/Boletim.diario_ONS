![dd](https://user-images.githubusercontent.com/84819715/224439920-61782684-1444-46bd-8072-8df203710c2c.png)


# Boletim.diario_ONS

O objetivo principal desse projeto é obter insights e previsões de aplicação prática para o setor de energia.
A ONS disponibiliza uma plataforma web para carregamento de dados situacionais em 3 versões.


# Versão 1 (100% - 12\03)
O objetivo principal da versão 1 é desenvolver uma estrutura automatizada segura para captar dados diários da ONS, realizar ETL nas tabelas e armazena-los em um banco em PostgreSQL.

### Etapa 1 - Automação de download com spam informativo no telegram ✔

### Etapa 2 - ETL em Python ✔

### Etapa 3 - Criação do banco de dados PostgreSQL ✔

### Etapa 4 - Alimentação do banco de dados de forma automatiza ✔



# Versão 2 (19/03)
O objetivo principal a versão 2 é utilizar os serviços da AWS para operar de forma segura (conteinerização docker) e estável.
![ONS project](https://user-images.githubusercontent.com/84819715/225630111-737d2828-76a8-44ea-bfae-f049e52fbf21.png)
https://lucid.app/lucidchart/d7d8a9fe-ca68-450a-9089-2d72ce54ecdb/edit?rtempr=1&page=eNbqbEM6f5NI&invitationId=inv_3b093e37-b59e-46a5-b6a7-82bb18c70eb0#
### Etapa 1 - Automação de download com lambda_AWS e armazenamento temporário S3 ✔

### Etapa 2 - ETL com lambda_AWS e armazenamento temporário S3 ✔
https://docs.aws.amazon.com/pt_br/AmazonRDS/latest/UserGuide/USER_PostgreSQL.S3Import.html
### Etapa 3 - Alimentação do rds



# Versão 3 (26/03)
O objetivo principal da versão 3 é integrar a api CCEE e implementar modelos de previsão por regressão e machine learn.

### Etapa 1 - Incremento da API CCEE (lambda e gateway)

### Etapa 2 - Previsões por regressão (Amazon SageMaker Model)

### Etapa 3 - ML (Amazon SageMaker Model)

### Etapa 4 - Visualização de dados (Amazon QuickSight)
