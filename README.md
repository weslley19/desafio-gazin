# Documentação da API

Documentação de uso da API.

Para acessar os endpoints que necessitam de autorização, envie no header da requisição o `Token de acesso` com o prefixo `Bearer`, por exemplo: 

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
 

## ENDPOINTS

*Desenvolvedor*
- [**Create**](#criar): /api/developers/
- [**Update**](#atualizar): /api/developers/{id}/
- [**ListAllDevelopers**](#dados-de-todos-os-desenvolvedores): /api/developers/
- [**ListDeveloper**](#desenvolvedor-especifico): /api/developers/{id}/
- [**Delete**](#deletar): /api/developers/{id}/

## Acesso

### Login

O login precisa de dois campos `username` e `password`.

- Endpoint: **/api/login/**
- Allowed method: POST
 
Para fazer login do usuário no sistema envie um POST ao endpoint e no corpo da requisição forneça as credencias do usuário tentando acessar o sistema nos campos `username` e `password`.

*POST*:

Corpo da requisição: JSON

```JSON
{
  "username": "login",
  "password": "senha",
}
```

Resposta:

*status_code*: 200
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwI...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b20cmVmcmVzaCIsImV4cCI6MTU4NTEzF..."
}
```

- `access`: Token utilizado como Authorization para acessar rotas privadas.
- `refresh`: Token com um tempo de vida maior para atualizar o Token de acesso.

### Refresh

- Endpoint: **/api/token/refresh/**
- Allowed method: POST
 
Para fazer gerar um novo token de acesso para um usuário sem precisar passar pela rota de Login novamente, você pode fazer uma requisição ao endpoint de refresh para receber um token novo de acesso e refresh com tempo de vida estendido. 

*Importante*: O token de `refresh` deve ser um token válido, ou seja, não pode ter expirado. Por esse motivo ele tem um tempo de vida maior do que o token de acesso.

Para renovar o Token, forneça os tokens de `access` e `refresh` atuais do usuário.

*POST*:

Corpo da requisição: JSON

```JSON
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwI...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b20cmVmcmVzaCIsImV4cCI6MTU4NTEzF...",
}
```

Resposta:

*status_code*: 200
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwI...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b20cmVmcmVzaCIsImV4cCI6MTU4NTEzF..."
}
```

- `access`: Token utilizado como Authorization para acessar rotas privadas.
- `refresh`: Token com um tempo de vida maior para atualizar o Token de acesso.


### Dados do desenvolvedor:

O endpoint de dados do desenvolvedor é útil para pegar os dados como *nome*, *data de nascimento*, entre outros dados referentes ao desenvolvedor vinculado ao token de acesso.

- Endpoint: **/api/developers/**
- Allowed method: GET
- Authorization necessária

Para pegar os dados do desenvolvedor deve ser feito uma requisição com o verbo http GET ao endpoint, e no header da requisição deve conter o campo de Authorization com o token de acesso Bearer válido do usuário.

*GET*:

Header

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIi...

Resposta:

*status_code*: 200
```json
{
    "id": 3,
    "created_at": "2021-11-01T21:44:28.574882-03:00",
    "updated_at": "2021-10-30T08:42:28.488682-03:00",
    "active": true,
    "name": "Weslley Oliveira",
    "sexo": "M",
    "age": 28,
    "hobby": "Jogar bola",
    "birthdate": "1999-10-21"
}
```

### Desenvolvedor especifico:

O endpoint para mostrar dados de um desenvolvedor em especifico é útil para pegar/atualizar os dados de um usuário como *nome*, *data de nascimento*, *idade*, entre outros dados referentes ao usuário de id igual ao repassado na url.

- Endpoint: **/api/developers/{id}/**
- Allowed method: GET
- Authorization necessária

Para pegar os dados do usuário deve ser feito uma requisição com o verbo http GET ao endpoint, e no header da requisição deve conter o campo de Authorization com o token de acesso JWT válido do usuário.

*GET*:

Header

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIi...

Resposta:

*status_code*: 200
```json
{
    "id": 3,
    "created_at": "2021-11-01T21:44:28.574882-03:00",
    "updated_at": "2021-10-30T08:42:28.488682-03:00",
    "active": true,
    "name": "Weslley Oliveira",
    "sexo": "M",
    "age": 28,
    "hobby": "Jogar bola",
    "birthdate": "1999-10-21"
}
```

### Criar desenvolvedor:

O endpoint para criar um desenvolvedor

- Endpoint: **/api/developers/**
- Allowed method: POST
- Authorization necessária

Para criar um desenvolvedor deve ser feito uma requisição com o verbo http POST ao endpoint, e no header da requisição deve conter o campo de Authorization com o token de acesso JWT válido do usuário.

*POST*:

Header

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIi...

Resposta:

*status_code*: 201
```json
{
    "id": 3,
    "created_at": "2021-11-01T21:44:28.574882-03:00",
    "updated_at": "2021-10-30T08:42:28.488682-03:00",
    "active": true,
    "name": "Weslley Oliveira",
    "sexo": "M",
    "age": 28,
    "hobby": "Jogar bola",
    "birthdate": "1999-10-21"
}
```

### Atualizar desenvolvedor:

O endpoint para atualizar um desenvolvedor

- Endpoint: **/api/developers/{id}/**
- Allowed method: POST
- Authorization necessária

Para atualizar um desenvolvedor deve ser feito uma requisição com o verbo http POST ao endpoint passando o id do desenvolvedor, e no header da requisição deve conter o campo de Authorization com o token de acesso JWT válido do usuário.

*POST*:

Header

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIi...

Resposta:

*status_code*: 200
```json
{
    "id": 3,
    "created_at": "2021-11-01T21:44:28.574882-03:00",
    "updated_at": "2021-10-30T08:42:28.488682-03:00",
    "active": true,
    "name": "Weslley Oliveira",
    "sexo": "M",
    "age": 28,
    "hobby": "Jogar bola",
    "birthdate": "1999-10-21"
}
```

### Deletar desenvolvedor:

O endpoint para deletar um desenvolvedor

- Endpoint: **/api/developers/{id}/**
- Allowed method: DELETE
- Authorization necessária

Para deletar um desenvolvedor deve ser feito uma requisição com o verbo http DELETE ao endpoint passando o id do desenvolvedor, e no header da requisição deve conter o campo de Authorization com o token de acesso JWT válido do usuário.

*POST*:

Header

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIi...

Resposta:

*status_code*: 204
```