from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, buscar_paciente_por_documento

if __name__ == "__main__":
    # Parámetros del paciente
    family_name = "Perez"
    given_name = "Juan"
    birth_date = "1990-01-01"
    gender = "male"
    phone = None 
    dni = "27182321"
    active = True

    # Crear y enviar el recurso de paciente
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone, dni, active)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient', url_alternativo = True)

    # Ver el recurso de paciente creado
    if patient_id:
        get_resource_from_hapi_fhir(patient_id, 'Patient', url_alternativo = True)

    # Buscar el paciente creado por su DNI
    paciente_encontrado = buscar_paciente_por_documento(dni, url_alternativo = True)
    print()
    print(paciente_encontrado)