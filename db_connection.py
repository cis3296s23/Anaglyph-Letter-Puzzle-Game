# load in public secrets
from dotenv import load_dotenv
from os import getenv

# connect to database
import firebase_admin
from firebase_admin import credentials, firestore

# get public secrets in memory
load_dotenv("./config/.env")

# use generated secrets to login into database 
cred = credentials.Certificate("./config/key.json")
firebase_admin.initialize_app(cred)

# get ref to databse
db = firestore.client()

# test user upload
# Get a reference to the 'users' collection
root_patient_coll_name = getenv('ROOT_PATIENT_COLLECTIONS')

patients_coll_ref = db.collection(root_patient_coll_name)

new_patients_ref = patients_coll_ref.document('p1')

new_patients_ref.set({
	'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30
})

