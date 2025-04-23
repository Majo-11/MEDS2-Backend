from connection import connect_to_mongodb
from bson import ObjectId
import json

collection = connect_to_mongodb("SamplePatientService", "patients")

def GetPatientById(patient_id: str):
    try:
        patient = collection.find_one({"_id": ObjectId(patient_id)})
        if patient:
            patient["_id"] = str(patient["_id"])
            return "success", patient
        return "notFound", None
    except Exception as e:
        return f"notFound", None

def WritePatient(patient_dict: dict):
    try:
        # Validar que el diccionario tenga los campos requeridos
        required_fields = ["nombres", "apellidos", "tipo_documento", "numero_documento", "telefono", "correo_electronico", "direccion", "ciudad", "localidad", "codigo_postal"]
        for field in required_fields:
            if field not in patient_dict:
                return f"errorValidating: Falta el campo requerido: {field}", None

        # Insertar el diccionario directamente en la base de datos
        result = collection.insert_one(patient_dict)
        if result:
            inserted_id = str(result.inserted_id)
            return "success", inserted_id
        else:
            return "errorInserting", None
    except Exception as e:
        return f"errorInserting: {str(e)}", None

def GetPatientByIdentifier(tipo_documento, numero_documento):
    try:
        patient = collection.find_one({"tipo_documento": tipo_documento, "numero_documento": numero_documento})
        if patient:
            patient["_id"] = str(patient["_id"])
            return "success", patient
        return "notFound", None
    except Exception as e:
        return f"error:{str(e)}", None