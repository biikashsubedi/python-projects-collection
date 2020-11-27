import phonenumbers
from phonenumbers import carrier, geocoder, timezone

phonenumber = input('Enter Phone Number: ')
number = phonenumbers.parse(phonenumber)

print(geocoder.description_for_number(number, 'en'))
print(carrier.name_for_number(number, 'en'))
print(timezone.time_zones_for_number(number))
