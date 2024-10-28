import re
import unidecode

from users.models import (
    User,
    Name,
    Coordinates,
    Timezone,
    Location,
    Picture,
    Contact,
)

class UserServices:

    @classmethod
    def get_region_user_from_state(cls, state: str) -> str:
        state = unidecode.unidecode(state)
        regions = {
            'centro-oeste': [
                'goias',
                'mato grosso',
                'mato grosso do sul',
                'distrito federal'],
            'norte': [
                'acre',
                'amapa',
                'amazonas',
                'para',
                'rondonia',
                'roraima',
                'tocantins'],
            'nordeste': [
                'alagoas',
                'bahia',
                'ceara',
                'maranhao',
                'piaui',
                'pernambuco',
                'paraiba',
                'rio grande do norte',
                'sergipe'],
            'sul': [
                'parana',
                'rio grande do sul',
                'santa catarina'],
            'sudeste': [
                'espirito santo',
                'minas gerais',
                'rio de janeiro',
                'sao paulo']
        }


        for key, values in regions.items():
            for value in values:
                if value == state.lower():
                    return key
        return 'desconhecido'

    @classmethod
    def get_type_user_from_region(cls, longitude: str, latitude: str) -> str:
        longitude = float(longitude)
        latitude = float(latitude)
        if 34.276938 <= abs(latitude) <= 52.997614 \
            and 2.196998 <= abs(longitude) <= 23.966413:
            return 'especial'

        elif 46.603598 <= abs(latitude) <= 54.777426 \
            and 26.155681 <= abs(longitude) <= 34.016466:
            return 'normal'
        else:
            return 'trabalhoso'

    @classmethod
    def create_users_from_data(cls, data_users: list) -> list:
        users_created = []
        for data in data_users:
            # Extrai os dados da requisicao
            name_data = data.get("name")
            location_data = data.get("location")
            picture_data = data.get("picture")
            contacts_data = {
                "email": data['email'],
                "phone": [cls.formatter_phone(data['phone'])],
                "cell": [cls.formatter_phone(data['cell'])]
            }
            gender_data = cls.formatter_gender(data.get("gender"))
            birthday = data.get("dob")['date']
            registered_data = data.get("registered")['date']
    
            #Type
            type_data = cls.get_type_user_from_region(longitude=location_data['coordinates']['longitude'],latitude=location_data['coordinates']['latitude'])
            # Criação de objetos relacionados
            name = Name.objects.create(**name_data)
            location_data['region'] = cls.get_region_user_from_state(state=location_data['state'])
            coordinates_data = location_data.pop("coordinates")
            timezone_data = location_data.pop("timezone")
    
            coordinates = Coordinates.objects.create(**coordinates_data)
            timezone = Timezone.objects.create(**timezone_data)
    
            location = Location.objects.create(
                coordinates=coordinates, timezone=timezone, **location_data
            )
            picture = Picture.objects.create(**picture_data)
    
            # Criar o usuário
            user = User.objects.create(
                name=name,
                location=location,
                picture=picture,
                type=type_data,
                gender=gender_data,
                birthday=birthday,
                registered=registered_data,
                nationality="BR",
            )
            users_created.append(user)
            contact = Contact.objects.create(
                user=user,
                **contacts_data
            )
        return users_created
        
    @classmethod
    def formatter_phone(cls, phone: str) -> str:
        return '+55' + re.sub('[^0-9]', '', phone)

    @classmethod
    def formatter_gender(cls, gender: str) -> str:
        return 'M' if gender == 'male' else 'F'


