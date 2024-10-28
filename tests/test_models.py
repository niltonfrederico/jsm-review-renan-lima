from django.test import TestCase
from model_bakery import baker

class ModelsTest(TestCase):

    def setUp(self) -> None:
        self.name = baker.make('users.Name')
        self.coordinates = baker.make('users.Coordinates')
        self.timezone = baker.make('users.Timezone')
        self.location = baker.make('users.Location')
        self.picture = baker.make('users.Picture')
        self.user = baker.make('users.User')

    def test_name_model_str_method(self):
        self.assertEqual(str(self.name), self.name.first)

    def test_coordinates_model_str_method(self):
        self.assertEqual(str(self.coordinates), f'{self.coordinates.latitude}, {self.coordinates.longitude}')

    def test_timezone_model_str_method(self):
        self.assertEqual(str(self.timezone), self.timezone.offset)

    def test_location_model_str_method(self):
        self.assertEqual(str(self.location), self.location.region)

    def test_picture_model_str_method(self):
        self.assertEqual(str(self.picture), self.picture.large)

    def test_user_model_str_method(self):
        self.assertEqual(str(self.user), self.user.name.first)