# Teste Case Juntos Somos Mais
## Intruções

Instale o Docker caso não tenha instalado na máquina. Execute o comando: "docker compose up" na raiz do projeto. Este comando subirá dois containers: Aplicação (Django) e banco de dados (Postgress). Após o processo, a API vai está disponível com todos os dados disponíveis nos endpoints.

O processo de subir os containers também definirá um superusuário (User: admin, Pass: admin) para ser usado nos endpoints POST que utilizam JWT. As rotas de listagem estão públicas para facilitar os testes (validate.sh).

## Endpoints
### Autenticação
Para obter o token de autenticação é preciso enviar um POST para /api/v1/token/ e recuperar o valor da chave *access*. 

![image](https://github.com/user-attachments/assets/034b422a-0f19-4676-8475-f9799624bbbc)

A API permite o envio de um arquivo ".csv" ou ".json" para adiconar registros no banco. É necessário adicionar um Authorization do tipo *Bearer Token* com a chave recuperada na rota de token.

![image](https://github.com/user-attachments/assets/9cf9175f-3f54-4dbe-9fdc-ad8eb2b23790)



