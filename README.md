# Teste Case Juntos Somos Mais
## Intruções

#### Instale o Docker 

Caso Não tenha instalado, é preciso instalar o Docker.

### Clone este repositório:

```
$ git clone https://github.com/7renan/challenge-juntos.git

```

#### Utilize o comando docker para disponibilizar todos os serviços, configurações e dados necessários para a aplicação:


```
docker compose up 
```
ou 

```
docker-compose up

```
#### Este comando usando docker já realiza todas as configurações, migrações e criações necessárias para disponibilizar os dados na API.

### Testes

Foram implementados testes unitários para garantir um bom funcionamento da aplicação.

![image](https://github.com/user-attachments/assets/4395cc92-85e5-46a2-83ba-5f8bcae0b617)


### Endpoints (Listagem)

#### Busca todos os usuários do banco permitindo alguns filtros:

 - Regiões do Brasil:
     - norte
     - nordeste
     - centro-oeste
     - sudeste
     - sul
 - Tipo:
    - especial
    - normal
    - trabalhoso

#### Busca todos
```
http://localhost:8080/api/v1/users/
``` 
![image](https://github.com/user-attachments/assets/43b60919-1a36-4375-88e4-f7ff27ae1f3d)


#### Busca todos da região norte
```
http://localhost:8080/api/v1/users/norte/
```
![image](https://github.com/user-attachments/assets/c3131fa8-7b40-45a9-9a10-4041eed859bb)


#### Busca todos do tipo especial
```
http://localhost:8080/api/v1/users/especial
```
![image](https://github.com/user-attachments/assets/40d6eaba-a260-46aa-83d3-a185e71c7e55)


#### Busca todos da região norte e também do tipo especial
```
http://localhost:8080/api/v1/users/norte/especial
```

![image](https://github.com/user-attachments/assets/18c53ed0-4e6d-432e-a5d5-d5e11d097724)


### Endpoints (Criação)
#### Para usar os endpoints de criação é necessários usar uma autenticação JWT. Para facilitar os testes, a aplicação cria um super usuário para ser usado.

#### Obter token de autenticação
```
127.0.0.1:8080/api/v1/token/
```
![image](https://github.com/user-attachments/assets/96028bc0-42e6-4654-b123-ebb3d8215197)


É preciso enviar no corpo da requisição o username (admin) e password(admin) para obter o valor da chave "access".

```
{
    "username": "admin",
    "password": "admin"
}
```

#### Enviar registros para serem criados no banco

```
http://localhost:8080/api/v1/users/create/
```
É necessário passar no Cabeçalho o token de autorização obtido anteriormente.
![image](https://github.com/user-attachments/assets/de5cfd5a-36bd-4d17-8c79-d1d23bc1f1ce)


É permitido enviar um arquivo ".json" ou ".csv"
![image](https://github.com/user-attachments/assets/7eae5e09-a296-462c-8687-49bf3f893c12)


Ou um json no corpo da requisição

![image](https://github.com/user-attachments/assets/a4b3bd79-eed1-47e3-8a6c-ebf76f90f583)






















