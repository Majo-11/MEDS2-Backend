from pymongo import MongoClient
from pymongo.server_api import ServerApi


def connect_to_mongodb(MedicationRequest, Medication
):
    uri = "mongodb+srv://mariajopineda:<a315-55g>@cluster0.7uchx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[MedicationRequest]
    collection = db[Medication]
    return collection
