# API AO PONTO - Documentação

Versão da API: 0.1.0

## Índice

- [Sobre a API](#sobre-a-api)
- [Endpoints](#endpoints)
  - [CardapioEscola](#cardapioescola)
  - [Salas](#salas)
  - [Usuário](#usuário)
  - [Escolas](#escolas)
  - [Turmas](#turmas)
  - [Login e Autenticação](#login-e-autenticação)
  - [AlunoTurmas](#alunoturmas)
  - [Papel](#papel)
- [Schemas](#schemas)

## Sobre a API

Esta documentação visa orientar o uso da API "AO PONTO", descrevendo os endpoints disponíveis e como interagir com eles. A versão atual da API é `0.1.0`.

## Endpoints

### CardapioEscola

#### GET `/v1/cardapio-escola/`

Retorna os dados do cardápio da escola. Possíveis parâmetros de consulta incluem tipo de busca (`all`), atributos específicos para busca (`attribute`, `value`), paginação (`skip`, `limit`) e autenticação via token no cabeçalho (`token`).

#### POST `/v1/cardapio-escola/`

Cria um novo registro no cardápio da escola. Requer um JSON com os dados do cardápio e, opcionalmente, autenticação via token no cabeçalho.

#### PUT `/v1/cardapio-escola/`

Atualiza um registro do cardápio da escola identificado por um UUID. Requer o UUID como parâmetro de consulta, um JSON com os dados atualizados e, opcionalmente, autenticação via token no cabeçalho.

#### DELETE `/v1/cardapio-escola/`

Deleta um registro do cardápio da escola identificado por um UUID. Requer o UUID como parâmetro de consulta e, opcionalmente, autenticação via token no cabeçalho.

### Salas

Endpoints para gerenciamento das salas seguem a mesma estrutura de operações que `CardapioEscola`.

### Usuário

Endpoints para gerenciamento de usuários, incluindo operações GET, POST, PUT, e DELETE, com parâmetros e autenticação similares aos descritos anteriormente.

### Escolas

Endpoints para gerenciamento das escolas, seguindo a mesma estrutura de `CardapioEscola`.

### Turmas

Endpoints para gerenciamento das turmas, seguindo a mesma estrutura de operações que `CardapioEscola`.

### Login e Autenticação

- POST `/v1/login/access-token`: Realiza login na aplicação, retornando um token de acesso.
- POST `/v1/forgot-my-password/`: Inicia o processo de recuperação de senha.
- POST `/v1/forgot-my-password/code`: Compara o código enviado por e-mail para validação.
- PUT `/v1/new-password/`: Permite a criação de uma nova senha após validação.

### AlunoTurmas

Endpoints para gerenciamento das relações aluno-turma, com operações de GET, POST, PUT e DELETE.

### Papel

Endpoints para gerenciamento dos papéis (roles) dos usuários, seguindo a mesma lógica de operações que `CardapioEscola`.

## Schemas

Os schemas detalham a estrutura dos objetos manipulados pela API. Para cada endpoint que requer ou retorna dados, um schema correspondente define os campos necessários e seus tipos.

---

Esta documentação é um resumo das funcionalidades da API "AO PONTO". Para informações mais detalhadas sobre cada endpoint, incluindo exemplos de requisições e respostas, consulte a documentação técnica completa.
