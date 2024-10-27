import os
import requests
import django

class SendDataAPI:
    def __init__(self):
        self.url_token = "http://127.0.0.1:8080/api/v1/token/"
        self.url_create_user = "http://127.0.0.1:8080/api/v1/users/create/"
        self.csv_url = 'https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv'
        self.json_url = 'https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json'
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'challenge_juntos.settings')
        django.setup()

    def get_token(self) -> str:
        payload = {
            "username": "admin",
            "password": "admin"
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic YWRtaW46YWRtaW4="
        }

        response = requests.post(self.url_token, json=payload, headers=headers)
        return response.json()['access']
    
    def send_data_to_api(self, file_content, file_name: str, file_type: str):
        headers = {
            "Authorization": f"Bearer {self.get_token()}"
        }

        files = {
            'file': (file_name, file_content, file_type)
        }

        response = requests.post(self.url_create_user, files=files, headers=headers)

        if response.status_code == 201:
            print("Dados carregados com sucesso ...")
        else:
            print("Erro ao carregar dados", response.status_code, response.json())

    def post_input_json(self):       
        json_response = requests.get(self.json_url)

        if json_response.status_code == 200:
            self.send_data_to_api(json_response.content, 'input-juntos.json', 'multipart/form-data')
            print("Sending data json ...")
        else:
            print("Erro ao carregar dados JSON:", json_response.status_code)

    def post_input_csv(self):       
        csv_response = requests.get(self.csv_url)

        if csv_response.status_code == 200:
            self.send_data_to_api(csv_response.content, 'input-juntos.csv', 'multipart/form-data')
            print("Sending data csv ...")
        else:
            print("Erro ao carregar dados o CSV:", csv_response.status_code)

if __name__ == "__main__":
    data_manager = SendDataAPI()
    data_manager.post_input_json()
    data_manager.post_input_csv()