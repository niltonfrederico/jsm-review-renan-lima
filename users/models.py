from turtle import ondrag
from django.core.validators import validate_email
from django.db import models


class Name(models.Model):
    title = models.CharField("Title", max_length=5)
    first = models.CharField("First Name", max_length=50)
    last = models.CharField("Last Name", max_length=50)

    class Meta:
        verbose_name = "Name"
        verbose_name_plural = "Names"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.first_name


class Coordinates(models.Model):
    latitude = models.CharField("Latitude", max_length=21)
    longitude = models.CharField("Longitude", max_length=21)

    class Meta:
        verbose_name = "Coordinates"
        verbose_name_plural = "Coordinates"
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.latitude}, {self.longitude}"


class Timezone(models.Model):
    offset = models.CharField("Offset", max_length=8)
    description = models.CharField("Description", max_length=150)

    class Meta:
        verbose_name = "Timezone"
        verbose_name_plural = "Time Zones"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.offset


class Location(models.Model):
    region = models.CharField("Region", max_length=15)
    street = models.CharField("Street", max_length=50)
    city = models.CharField("City", max_length=50)
    state = models.CharField("State", max_length=30)
    postcode = models.IntegerField("Postcode")
    coordinates = models.ForeignKey(
        Coordinates, on_delete=models.CASCADE, related_name="locations"
    )
    timezone = models.ForeignKey(
        Timezone, on_delete=models.CASCADE, related_name="locations"
    )

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.region


class Picture(models.Model):
    large = models.URLField("Large Image URL", max_length=255)
    medium = models.URLField("Medium Image URL", max_length=255)
    thumbnail = models.URLField("Thumbnail Image URL", max_length=255)

    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.large


class User(models.Model):
    type = models.CharField("Type", max_length=50, default="")
    gender = models.CharField("Gender", max_length=10)
    name = models.ForeignKey(Name, on_delete=models.CASCADE, related_name="customers")
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="customers"
    )
    birthday = models.CharField("Birthday", max_length=50)
    registered = models.CharField("Registration Date", max_length=50)

    picture = models.ForeignKey(
        Picture, on_delete=models.CASCADE, related_name="customers"
    )
    nationality = models.CharField("Nationality", max_length=2, default="BR")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.name.first_name

    def get_contacts(self):
        """
        Retorna uma lista de dicionários com as informações de contato do usuário.
        """
        return [
            {
                "email": contact.email,
                "phone": contact.phone,
                "cell": contact.cell,
            }
            for contact in self.contacts.all()
        ]


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    email = models.EmailField("E-mail", max_length=50, validators=[validate_email])
    phone = models.JSONField(default=list, verbose_name="Telephone Numbers")
    cell = models.JSONField(default=list, verbose_name="Mobile Numbers")

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ["id"]
