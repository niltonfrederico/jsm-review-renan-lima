import os
import requests
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'challenge_juntos.settings')
django.setup()

from django.core.files.uploadedfile import SimpleUploadedFile
# models
from users.services.user_services import UserServices
from users.services.data_services import DataServices

class SendDataAPI:
    def __init__(self):
        self.csv_url = 'https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv'
        self.json_url = 'https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json'

    def load_data_input(self) -> list:
        json_response = requests.get(self.json_url)
        csv_response = requests.get(self.csv_url)

        if json_response.status_code == 200 and csv_response.status_code == 200:
            json_upload = SimpleUploadedFile(
                name="input-juntos.json",
                content=json_response.content,
                content_type="multipart/form-data"      
            )

            csv_upload = SimpleUploadedFile(
                name="input-juntos.json",
                content=json_response.content,
                content_type="multipart/form-data"      
            )

        # create users from json
        data_users_json = DataServices.load_file(data_file=json_upload)
        UserServices.create_users_from_data(data_users=data_users_json)
        print(f"{len(data_users_json)} registros json carregados com sucesso ...")

        # create users from csv
        data_users_csv = DataServices.load_file(data_file=csv_upload)
        UserServices.create_users_from_data(data_users=data_users_csv)
        print(f"{len(data_users_csv)} registros csv carregados com sucesso ...")

if __name__ == "__main__":
    data_manager = SendDataAPI()
    data_manager.load_data_input()