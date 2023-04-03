import asyncio # to run async coroutines

# load in public secrets
from dotenv import load_dotenv
from os import getenv

# connect to database
import firebase_admin
from google.cloud.firestore import Client as Firestore
from firebase_admin import credentials, firestore_async

# get public secrets in memory
load_dotenv("./config/.env")

# use generated secrets to login into database 
cred = credentials.Certificate("./config/key.json")

class FirebaseConnection():
    def __init__(self, username: str) -> None:
        # init firebase connection via secrets file
        firebase_admin.initialize_app(cred)
        # get ref to databse
        self.db: Firestore = firestore_async.client()
        self.username = username

    async def test(self):
        """test database connection by uploading a default dict to the firebase document under `self.username`
        """

        # test user upload
        root_patient_coll_name = getenv('ROOT_PATIENT_COLLECTIONS')

        if root_patient_coll_name is None:
            raise ValueError("collection value not found, check .env")

        # get collection ref 
        patients_coll_ref = self.db.collection(root_patient_coll_name)

        # use collection to create document ref
        new_patients_ref = patients_coll_ref.document(self.username)

        # start saving document
        result = new_patients_ref.set({
            'name': 'John Doe',
            'email': 'john@example.com',
            'age': 30
        })

        return await result


FBC = FirebaseConnection('TestUser1')
asyncio.run(FBC.test())

        