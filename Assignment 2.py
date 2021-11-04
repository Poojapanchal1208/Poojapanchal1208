from collections import defaultdict

welcome_screen_message = """"""

def get_user_information():
    customer = defaultdict(dict)

    customer['name']['first_name'] = input('Enter First Name: ')
    customer['name']['last_name'] = input('Enter Last Name: ')
    customer['delivery_address']['street_number'] = input('Enter Street Number:')
    customer['delivery_address']['street_name'] = input('Enter Street name: ')
    customer['delivery_address']['unit'] = input('Enter unit number: ') or ''
    customer['address']['city'] = input('Enter City name: ')
    customer['address']['province'] = input('Enter province: ')
    customer['address']['postal_code'] = input('Enter postal code: ')
    customer['special_instructions'] = input('Enter instructions: ')
    customer['phone_number'] = input('Enter phone number: ')

    return customer