from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, buscar_paciente_por_documento
from fhir.resources.identifier import Identifier

if __name__ == "__main__":
    # Parámetros del paciente (se puede dejar algunos vacíos)
    family_name = "Perez"
    given_name = "Juan"
    birth_date = "1990-01-01"
    gender = "male"
    phone = None 
    dni = "27182321"

    """
    identifier = {
        "use" : "usual",
        "type" : None,
        "system" : None,
        "value" : "27182321",
        "period" : None,
        "assigner" : None
    }
    """

    # Crear y enviar el recurso de paciente
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone, dni)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')

    # Ver el recurso de paciente creado
    if patient_id:
        get_resource_from_hapi_fhir(patient_id,'Patient')

    paciente_encontrado = buscar_paciente_por_documento(dni)
    print()
    print(paciente_encontrado)