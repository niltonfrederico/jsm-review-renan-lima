from rest_framework import serializers
from users.models import (
    User,
    Name,
    Coordinates,
    Timezone,
    Location,
    Picture,
    Contact,
)


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ("large", "medium", "thumbnail")


class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = (
            "offset",
            "description",
        )


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = (
            "latitude",
            "longitude",
        )


class LocationSerializer(serializers.ModelSerializer):
    coordinates = CoordinatesSerializer(read_only=True)
    timezone = TimezoneSerializer(read_only=True)

    class Meta:
        model = Location
        fields = (
            "region",
            "street",
            "city",
            "state",
            "postcode",
            "coordinates",
            "timezone",
        )


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = (
            "title",
            "first",
            "last",
        )


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            "email",
            "phone",
            "cell",
        )


class UserSerializer(serializers.ModelSerializer):
    name = NameSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    picture = PictureSerializer(read_only=True)
    contacts = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "type",
            "gender",
            "name",
            "location",
            "birthday",
            "registered",
            "picture",
            "nationality",
            "contacts",
        ]

    def get_contacts(self, obj):
        return obj.get_contacts()