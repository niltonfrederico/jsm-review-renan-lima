# Teste Case Juntos Somos Mais
## Intruções

Instale o Docker caso não tenha instalado na máquina. Execute o comando: "docker compose up" na raiz do projeto. Este comando subirá dois containers: Aplicação (Django) e banco de dados (Postgress). Após o processo, a API vai está disponível com todos os dados disponíveis nos endpoints.

O processo de subir os containers também definirá um superusuário (User: admin, Pass: admin) para ser usado nos endpoints POST que utilizam JWT. As rotas de listagem estão públicas para facilitar os testes (validate.sh).

## Endpoints
### Autenticação
![image](https://github.com/user-attachments/assets/93e7821f-d355-44e2-afb4-9af1ac64ed6c)



 
