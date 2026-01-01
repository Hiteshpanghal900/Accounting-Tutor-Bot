import firebase_admin
from firebase_admin import firestore, credentials

cred = credentials.Certificate("./firestore.json")

firebase_admin.initialize_app(cred)
db = firestore.client()
