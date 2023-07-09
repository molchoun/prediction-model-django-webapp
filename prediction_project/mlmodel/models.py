from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class ZeroOneBooleanField(models.BooleanField):


    def from_db_value(self, value, expression, connection, context=None):
        if value is None:
            return value
        return int(value)


def get_or_create_public_user():
    user = get_user_model()
    try:
        public_user = user.objects.get(username='public')
    except user.DoesNotExist:
        public_user = user.objects.create_user(username='public')
    return public_user


class House(models.Model):

    class ConstructionType(models.TextChoices):
        STONE = 'Stone', 'Stone'
        PANEL = 'Panels', 'Panels'
        MONOLITH = 'Monolith', 'Monolith'
        CASSETTE = 'Cassette', 'Cassette'
        WOOD = 'Wooden', 'Wooden'
        BRICK = 'Bricks', 'Bricks'

    class Balcony(models.TextChoices):
        OPEN = 'Open balcony', 'Open balcony'
        CLOSED = 'Closed balcony', 'Closed balcony'
        NO = 'Not available', 'Not available'
        MULTIPLE = 'Multiple balconies', 'Multiple balconies'

    class Furniture(models.TextChoices):
        AVAILABLE = 'Available', 'Available'
        NO = 'Not available', 'Not available'
        BY_AGREEMENT = 'By agreement', 'By agreement'
        PARTIAL = 'Partial Furniture', 'Partial Furniture'

    class Renovation(models.TextChoices):
        MAJOR = 'Major Renovation', 'Major Renovation'
        EURO = 'Euro Renovation', 'Euro Renovation'
        OLD = 'Old Renovation', 'Old Renovation'
        NO = 'No Renovation', 'No Renovation'
        DESIGNER = 'Designer Renovation', 'Designer Renovation'
        PARTIAL = 'Partial Renovation', 'Partial Renovation'
        COSMETIC = 'Cosmetic Renovation', 'Cosmetic Renovation'

    construction_type = models.CharField(
        max_length=8,
        choices=ConstructionType.choices,
    )
    new_construction = ZeroOneBooleanField()
    elevator = ZeroOneBooleanField()
    floors_in_the_building = models.SmallIntegerField()
    floor_area = models.FloatField()
    number_of_rooms = models.SmallIntegerField()
    number_of_bathrooms = models.SmallIntegerField()
    ceiling_height = models.FloatField()
    floor = models.SmallIntegerField()
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    balcony = models.CharField(
        max_length=18,
        choices=Balcony.choices
    )
    furniture = models.CharField(
        max_length=20,
        choices=Furniture.choices,
    )
    renovation = models.CharField(
        max_length=24,
        choices=Renovation.choices
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='house',
        default=get_or_create_public_user
    )
    prediction = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self):
        return f"House on {self.address}"



