from django.core.cache import cache
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from users.models import User
from users.api.serializers import UserSerializer
from users.models import User

# services
from ..services.user_services import UserServices
from ..services.data_services import DataServices

# exceptions
from json import JSONDecodeError
from csv import Error as ErrorCSV
from ..exceptions.invalid_file_exception import InvalidFileTypeError


class UsersListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    user_services = UserServices

    def get_queryset(self):
        cache_key = "users_queryset"
        queryset = cache.get(cache_key)

        if not queryset:
            queryset = User.objects.all()
            cache.set(cache_key, queryset, timeout=600)

        region = self.kwargs.get("region")
        type = self.kwargs.get("type")
        region_or_type = self.kwargs.get("region_or_type")

        if region and type:
            return self.queryset.filter(
                type=type,
                location__region=region
            )

        if region_or_type:
            region_queryset = self.queryset.filter(
                location__region=region_or_type
            )
            if region_queryset:
                return region_queryset

            return self.queryset.filter(
                type=region_or_type
            )

        return queryset


class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"  # O campo que será usado para buscar o item (ID)

    def get_object(self):
        # Define a chave de cache única para o usuário
        user_id = self.kwargs.get(self.lookup_field)
        cache_key = f"user_{user_id}"
        user = cache.get(cache_key)

        if not user:
            # Carrega o usuário do banco de dados se o cache estiver vazio
            user = User.objects.filter(id=user_id).first()  # Busca o usuário pelo ID

            if user:
                # Armazena o usuário no cache por 10 minutos (600 segundos)
                cache.set(cache_key, user, timeout=600)

        if user is None:
            raise Http404  # Lança um erro 404 se o usuário não for encontrado

        return user


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
 
    def create(self, request, *args, **kwargs):
        data_users = None
        # verifica o envio de um arquivo json
        if 'file' in request.FILES:
            file = request.FILES['file']
            try:
                data_users = DataServices.load_file(data_file=file)
            except JSONDecodeError:
                return Response(
                    {"error": "O arquivo não é um JSON válido."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            except ErrorCSV:
                return Response(
                    {"error": "O arquivo não é um CSV válido."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            except InvalidFileTypeError:
                return Response(
                    {"error": "O arquivo não possui um formato válido. Envie no formato '.csv' ou '.json' "},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
        else:
            data_users = data_users if isinstance(data_users, list) else [request.data]

        users_created = UserServices.create_users_from_data(data_users)
        # Utilize o serializer apenas para validar e retornar os dados
        serializer = self.get_serializer(users_created, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)