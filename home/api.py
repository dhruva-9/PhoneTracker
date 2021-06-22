import phonenumbers
from phonenumbers import geocoder, carrier
from phonenumbers.phonenumber import PhoneNumber
from phonenumbers.phonenumberutil import region_code_for_number

def api(number):
    phoneNumber = phonenumbers.parse(number, 'IN')

    valid = phonenumbers.is_valid_number(phoneNumber)

    if valid == False:
        return valid

    else:
        Carrier = carrier.name_for_number(phoneNumber, 'en')
        Region = geocoder.country_name_for_number(phoneNumber, 'en')
        return Carrier, Region