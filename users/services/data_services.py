import json, csv
from django.core.files.uploadedfile import UploadedFile

# esceptions
from ..exceptions.invalid_file_exception import InvalidFileTypeError
class DataServices:

    @staticmethod
    def load_json(file: UploadedFile):
        pass

    @classmethod
    def load_file(cls, data_file: UploadedFile):
        if data_file.name.endswith('.json'):
            try:
                data_users = json.load(data_file)
                print(f"{len(data_users)} files json")
                return data_users['results']
            except json.JSONDecodeError:
                raise 
        
        elif data_file.name.endswith('.csv'):
            try:
                data_csv = data_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(data_csv, quotechar='"')
                data_users = [cls.format_data_users(data_user=row) for row in reader]
                print(f"{len(data_users)} files csv")
                return data_users
            except csv.Error:
                raise
        
        else:

            raise InvalidFileTypeError("Tipo de arquivo nao suportado.")
        
    @staticmethod    
    def format_data_users(data_user: dict):
        
        dict_formated = {}

        for key, value in data_user.items():
            # Remove o caractere ufeff
            clean_key = key.replace('\ufeff', '').strip('"')
            keys = clean_key.split('__')
            current_level = dict_formated
            
            for k in keys[:-1]:
                if k not in current_level:
                    current_level[k] = {}
                current_level = current_level[k]
            
            current_level[keys[-1]] = value

        return dict_formated



