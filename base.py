import requests
from patient import create_patient_resource


# Enviar el recurso FHIR al servidor HAPI FHIR
def send_resource_to_hapi_fhir(resource, resource_type, url_alternativo = False):
    if url_alternativo:
        url = f"https://launch.smarthealthit.org/v/r4/fhir/{resource_type}"
    else:
        url = f"http://hapi.fhir.org/baseR5/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}
    resource_json = resource.json()

    response = requests.post(url, headers=headers, data=resource_json)

    if response.status_code == 201:
        print("Recurso creado exitosamente")
        
        # Devolver el ID del recurso creado
        return response.json()['id']
    else:
        print(f"Error al crear el recurso: {response.status_code}")
        print(response.json())
        return None


# Buscar el recurso por ID 
def get_resource_from_hapi_fhir(resource_id, resource_type, url_alternativo = False):
    if url_alternativo:
        url = f"https://launch.smarthealthit.org/v/r4/fhir/{resource_type}/{resource_id}"
    else:
        url = f"http://hapi.fhir.org/baseR5/{resource_type}/{resource_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.json())


def buscar_paciente_por_documento(numero_documento, url_alternativo = False):
    if url_alternativo:
        url = f"https://launch.smarthealthit.org/v/r4/fhir/Patient?identifier={numero_documento}"
    else:
        url = f"http://hapi.fhir.org/baseR5/Patient?identifier={numero_documento}"
    #response = requests.get(url)
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        data = response.json()
        if data.get("total", 0) > 0:
            return data["entry"][0]["resource"]  # Retorna el primer paciente encontrado
        else:
            return "Paciente no encontrado"
    else:
        return f"Error en la solicitud: {response.status_code}"