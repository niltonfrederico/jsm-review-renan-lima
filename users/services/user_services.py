import unidecode

class UserServices:

    @classmethod
    def get_region_user_from_state(self, state: str) -> str:
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
    def get_type_user_from_region(self, longitude: str, latitude: str) -> str:
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
