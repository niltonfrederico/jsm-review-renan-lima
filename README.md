# Teste Case Juntos Somos Mais
## Intruções

### Instale o Docker 

Caso Não tenha instalado, é preciso instalar o Docker.

### Clone este repositório:

```
$ git clone https://github.com/7renan/challenge-juntos.git

```

### Utilize o comando docker para disponibilizar todos os serviços, configurações e dados necessários para a aplicação:


```
docker compose up 
```
ou 

```
docker-compose up

```

### Testes

Foram implementados testes unitários para garantir um bom funcionamento da aplicação.

![alt text](image.png)

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
![alt text](image-1.png)

#### Busca todos da região norte
```
http://localhost:8080/api/v1/users/norte/
```
![alt text](image-2.png)

#### Busca todos do tipo especial
```
http://localhost:8080/api/v1/users/especial
```
![alt text](image-3.png)

#### Busca todos da região norte e também do tipo especial
```
http://localhost:8080/api/v1/users/norte/especial
```

![alt text](image-4.png)

### Endpoints (Criação)
#### Para usar os endpoints de criação é necessários usar uma autenticação JWT. Para facilitar os testes, a aplicação cria um super usuário para ser usado.

#### Obter token de autenticação
```
127.0.0.1:8080/api/v1/token/
```
![alt text](image-5.png)

É preciso enviar no corpo da requisição o username (admin) e password(admin) para obter o valor da chave "acceess".

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
![alt text](image-6.png)

É permitido enviar um arquivo ".json" ou ".csv"
![alt text](image-7.png)

Ou um json no corpo da requisição

![alt text](image-8.png)





















