from django.core.validators import RegexValidator


def city_name_validator(value):
    validated = RegexValidator(
        regex=r'^[-а-яА-Я]+$',
        message='Название города должно содержать только русские буквы.'
    )(value)
    return validated
