from device import create_device_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir

if __name__ == "__main__":
    # Parámetros del dispositivo
    device_name = "Ecógrafo"
    status = "active"
    manufacturer = "Ultraschall S.A."
    model_number = "1328"
    manufacture_date = "2019-03-10"
    expiration_date = "2025-03-10"
    id = "12345"

    # Crear y enviar el recurso de dispositivo
    device = create_device_resource(device_name, status, manufacturer, model_number, manufacture_date, expiration_date, id)
    device_id = send_resource_to_hapi_fhir(device, 'Device', url_alternativo = True)

    # Ver el recurso de dispositivo creado
    if device_id:
        get_resource_from_hapi_fhir(device_id, 'Device', url_alternativo = True)