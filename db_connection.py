# to run async coroutines
import asyncio 

# get epoch time
import time    

# load in public secrets
from dotenv import load_dotenv
from os import getenv

# connect to database
import firebase_admin
from firebase_admin import credentials, firestore_async

# using this to provide type suggestions
from google.cloud.firestore import Client as Firestore
from google.cloud.firestore_v1.document import DocumentReference


# get public secrets in memory
load_dotenv("./config/.env")

# use generated secrets to login into database 
cred = credentials.Certificate("./config/key.json")

"""
save color data
save data function
"""

class FirebaseConnection():
    """`FirebaseConnection` provides a set of functions to communicate with the predefined database based on app secrets.
    It uses `firestore_async` to do so. 
    """
    def __init__(self, username: str) -> None:
        # init firebase connection via secrets file
        firebase_admin.initialize_app(cred)
        # get ref to databse
        self.db: Firestore = firestore_async.client()
        self.username = username

        self.patients_collection = getenv('ROOT_PATIENT_COLLECTIONS')

        if self.patients_collection is None:
            raise ValueError("collection value not found, check .env")


    def save_time(self, docRef: DocumentReference):
        return docRef.set({ 'lastUpdated': int(time.time()) }, merge=True)
        

    async def test(self):
        """test database connection by uploading a default dict to the firebase document under `self.username`
        """
        # get collection ref 
        patients_coll_ref = self.db.collection(self.patients_collection)

        # use collection to create document ref
        new_patients_ref = patients_coll_ref.document(self.username)

        # start saving document
        result = new_patients_ref.set({
            'name': 'John Doe',
            'email': 'john@example.com',
            'age': 30
        }, merge=True)

        await self.save_time(new_patients_ref)

        return await result


FBC = FirebaseConnection('TestUser1')
asyncio.run(FBC.test())

        