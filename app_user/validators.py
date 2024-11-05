import random
from django.core.exceptions import ValidationError


def generate_random_key():
    return random.randint(1000, 9999)


def validate_nid(value):
    if len(str(value)) != 10:
        raise ValidationError("NID must be 10 digits long.")


def validate_phone_number(value):
    if len(value) != 14:
        raise ValidationError("Phone number must be 11digits long.")
