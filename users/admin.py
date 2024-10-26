from django.contrib import admin
from .models import Name, Coordinates, Timezone, Location, Picture, User, Contact


@admin.register(Name)
class NameModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "first",
        "last",
    )


@admin.register(Coordinates)
class CoordinatesModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "latitude",
        "longitude",
    )


@admin.register(Timezone)
class TimezoneModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "offset",
        "description",
    )


@admin.register(Location)
class LocationModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "region",
        "street",
        "city",
        "state",
        "postcode",
        "coordinates",
        "timezone",
    )


@admin.register(Picture)
class PictureModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "large",
        "medium",
        "thumbnail",
    )


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "type",
        "gender",
        "name",
        "location",
        "birthday",
        "registered",
        "picture",
        "nationality",
    )


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "cell", "user")
