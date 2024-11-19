# Creación del recurso Patient

```python
def create_patient_resource(family_name=None, given_name=None, birth_date=None, gender=None, phone=None, dni=None, active=None):
    patient = Patient()
    
    if family_name or given_name:
        name = HumanName()
        if family_name:
            name.family = family_name
        if given_name:
            name.given = [given_name]
        patient.name = [name]
    
    if birth_date:
        patient.birthDate = birth_date

    if gender:
        patient.gender = gender

    if phone:
        contact = ContactPoint()
        contact.system = "phone"
        contact.value = phone
        contact.use = "mobile"
        patient.telecom = [contact]

    if dni:
        identifier = Identifier()
        identifier.value = dni
        patient.identifier = [identifier]

    if active:
        patient.active = active

    return patient
```

# Envío del recurso creado al servidor

```python
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
```

## Lectura del recurso creado

```python
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
```

## Función de búsqueda de paciente por DNI

```python
def buscar_paciente_por_documento(numero_documento, url_alternativo = False):
    if url_alternativo:
        url = f"https://launch.smarthealthit.org/v/r4/fhir/Patient?identifier={numero_documento}"
    else:
        url = f"http://hapi.fhir.org/baseR5/Patient?identifier={numero_documento}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        data = response.json()
        if data.get("total", 0) > 0:
            return data["entry"][0]["resource"]  # Retorna el primer paciente encontrado
        else:
            return "Paciente no encontrado"
    else:
        return f"Error en la solicitud: {response.status_code}"
```
