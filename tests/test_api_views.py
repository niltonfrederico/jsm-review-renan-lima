import requests
from django.urls import reverse
from rest_framework.test import APITestCase

import os
import requests
import django

from django.core.files.uploadedfile import SimpleUploadedFile
# models
from users.services.user_services import UserServices
from users.services.data_services import DataServices

class ApiTestcase(APITestCase):

    def setUp(self):
        self.url_list = reverse('users-list')
        self.url_region = reverse('users-region-or-type', kwargs={'region_or_type': 'norte'})
        self.url_type = reverse('users-region-or-type', kwargs={'region_or_type': 'trabalhoso'})
        self.url_type_and_region = reverse('users-region-and-type', kwargs={'region': 'norte', 'type':'trabalhoso'})
        self.csv_url = 'https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv'
        self.json_url = 'https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json'

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
        UserServices.create_users_from_data(data_users=data_users_json[:10])

        # create users from csv
        data_users_csv = DataServices.load_file(data_file=csv_upload)
        UserServices.create_users_from_data(data_users=data_users_csv[:10])
    
    def test_users_detail(self):
        pass

    def test_users_list(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, 200)

    def test_users_filter_by_region_or_type(self):
        response_region = self.client.get(self.url_region)
        response_type = self.client.get(self.url_type)

        self.assertEqual(response_type.data['users'][0]['type'], 'trabalhoso')
        self.assertEqual(response_region.data['users'][0]['location']['region'], 'norte')


    def test_users_filter_by_region_and_type(self):
        response_region_and_type = self.client.get(self.url_type_and_region)
        self.assertEqual(response_region_and_type.data['users'][0]['type'], 'trabalhoso')
        self.assertEqual(response_region_and_type.data['users'][0]['location']['region'], 'norte')
