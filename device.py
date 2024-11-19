from fhir.resources.device import Device
from fhir.resources.identifier import Identifier

def create_device_resource(name=None, status=None, manufacturer=None, model_number=None, manufacture_date=None, expiration_date=None, id=None):
    device = Device()
    
    if name:
        device.displayName = name

    if status:
        device.status = status
    
    if manufacturer:
        device.manufacturer = manufacturer

    if model_number:
        device.modelNumber = model_number

    if manufacture_date:
        device.manufactureDate = manufacture_date

    if expiration_date:
        device.expirationDate = expiration_date

    if id:
        identifier = Identifier()
        identifier.value = id
        device.identifier = [identifier]

    return device