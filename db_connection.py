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

class FirebaseConnection():
    def __init__(self, username: str) -> None:
        # init firebase connection via secrets file
        firebase_admin.initialize_app(cred)
        # get ref to databse
        self.db = firestore.client()
        self.username = username

    def __test(self):
        """test database connection by uploading a default dict to the firebase document under `self.username`
        """

        # test user upload
        root_patient_coll_name = getenv('ROOT_PATIENT_COLLECTIONS')

        # get collection ref 
        patients_coll_ref = self.db.collection(root_patient_coll_name)

        # use collection to create document ref
        new_patients_ref = patients_coll_ref.document(self.username)

        # set document
        new_patients_ref.set({
            'name': 'John Doe',
            'email': 'john@example.com',
            'age': 30
        })

FBC = FirebaseConnection('TestUser1')
FBC.__test()

        