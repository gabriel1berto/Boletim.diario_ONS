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

Antes de qualquer projeto na aws é interessante desenhar uma arquitetura básica e criar funções AIM para liberar movimentações de dados e requisições de acessos de funções lambda à bancos de dados. 
![ONS project](https://user-images.githubusercontent.com/84819715/225630111-737d2828-76a8-44ea-bfae-f049e52fbf21.png)

https://lucid.app/lucidchart/d7d8a9fe-ca68-450a-9089-2d72ce54ecdb/edit?rtempr=1&page=eNbqbEM6f5NI&invitationId=inv_3b093e37-b59e-46a5-b6a7-82bb18c70eb0#

### Etapa 1 - Automação de download com lambda_AWS e armazenamento temporário S3 ✔
lambda1_ons_aws.inpy

![Captura de tela 2023-03-24 170502](https://user-images.githubusercontent.com/84819715/227633767-a265f3c2-8ff2-4b37-bff0-42c1a935903e.png)





### Etapa 2 - ETL com lambda_AWS e armazenamento temporário S3 ✔
lambda2_ons_aws.inpy

https://docs.aws.amazon.com/pt_br/AmazonRDS/latest/UserGuide/USER_PostgreSQL.S3Import.html
### Etapa 3 - Alimentação do rds
![Captura de tela 2023-03-24 173705](https://user-images.githubusercontent.com/84819715/227633911-2be44a33-9152-4578-9d5b-ce424ff1ca80.png)



# Versão 3 (26/03)
O objetivo principal da versão 3 é integrar a api CCEE e desevolver previsões.

### Etapa 1 - Incremento de APIs do setor (lambda e gateway)
API ONS - https://portal-integra.ons.org.br/api-docs (https://www.google.com/search?sxsrf=AJOqlzWp4ZWA-0o_ovykGFh5-TDKAkCERA:1679070436242&q=requisi%C3%A7%C3%B5es+de+api+ons&spell=1&sa=X&ved=2ahUKEwidsZ7nsOP9AhURr5UCHW95BUMQBSgAegQICBAB&biw=985&bih=938&dpr=0.94#fpstate=ive&vld=cid:96f19c9f,vid:ZHH2qEh990g)
API MLE - 
API PEE -
API ANEEL -
