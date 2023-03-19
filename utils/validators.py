from django.core.validators import RegxValidator

class PhoneNumberValidator(RegxValidator):
    regex = '^98(9[0-3,9\d{8}]|[1-9]\d{9})$'
    message = 'Phone number must be a VALID 12 digits like 98xxxxxxxxxx'
    code = 'invalid_phone_number'

class SKUValidators(RegxValidator):
    regex = '^[a-zA-Z0-9\-\_]{6,20}$'
    message = 'SKU must be alphanumeric with 6 tot 20 characters'
    code = 'invalid_sku' 

class UsernameValidators(RegxValidator):
    regex = '^[a-zA-Z][a-zA-Z0-9_\.]+$'
    message = _('Enter a valid username starting with a-z.'
                'This value any contain onliy letters, numbers and underscor characters')
    code = 'Invalid_username'
class PostalCodeValidator(RegxValidator):
    regex = '^[0-9](10)$'
    message = _('Enter a valid postal coce')
validate_phone_number = PhoneNumberValidator()
validate_sku = SKUValidators()
validate_username = UsernameValidators()
validate_postalcode = PostalCodeValidator()
  