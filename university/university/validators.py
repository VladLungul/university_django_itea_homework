import re


def my_validator(self, val, value_valid):
    is_match = value_valid.search(val)
    return is_match

first_name_valid = re.compile(r'^[A-z]+\ ?[A-z]?$')
phone_valid = re.compile(r'\+380\d{9}')
last_name_valid = re.compile(r'^[A-z]+\-?[A-z]?$')


def clean(self):
    if not self.my_validator(self.phone_number, self.phone_valid):
        logger.warning('bad user, wrong data number')
        raise ValidationError('not correct number')
    if not self.my_validator(self.first_name, self.first_name_valid):
        logger.warning('bad user, wrong data first name')
        raise ValidationError('not correct first name')
    if not self.my_validator(self.last_name, self.last_name_valid):
        logger.warning('bad user, wrong data last name')
        raise ValidationError('not correct last_name')


