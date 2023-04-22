# to run async coroutines
import asyncio 

# get epoch time
import time    

# load in public secrets
from dotenv import load_dotenv
from os import getenv

# connect to database
import firebase_admin
from firebase_admin import credentials, firestore

# using this to provide type suggestions
from google.cloud.firestore import Client as Firestore
from google.cloud.firestore_v1.document import DocumentReference, DocumentSnapshot

# typing
from typing import Union, Dict

# loading env for website
load_dotenv("../anaglyph-letter-puzzle-game-frontend/.env")

# use generated secrets to login into database 
cred = credentials.Certificate("../config/key.json")

class FirebaseConnection():
    """`FirebaseConnection` provides a set of functions to communicate with the predefined database based on app secrets.
    It uses `firestore` to do so. [SYNC] 

    FirebaseConnection is NOT stateless. Once `login()` is called, the side effects are based on the data passed in.
    """
    def __init__(self) -> None:
        # init firebase connection via secrets file
        firebase_admin.initialize_app(cred)
        # get ref to databse
        self.db: Firestore = firestore.client()
        self.user_ref: Union[DocumentReference, None] = None

        if getenv("NEXT_PUBLIC_ROOT_USER_COLLECTION") is None:
            raise ValueError(".env var NEXT_PUBLIC_ROOT_USER_COLLECTION not found")


    def stamp_time(self, docRef: Union[DocumentReference, None]=None):
        """attach a timestamp to a document ref

        Args:
            docRef (DocumentReference, optional): ref of doc that needs a timestamp update.\n
            If none, user user_ref
        """

        if self.user_ref is None and docRef is None:
            raise ValueError("User not logged in and no provided doc_ref")

        doc_to_stamp: DocumentReference = self.user_ref if docRef is None else docRef
        return doc_to_stamp.set({ 'lastUpdated': int(time.time()) }, merge=True)
        

    def login(self, username: str, password: str) -> bool:
        """Login method with side effects (saves user document to `self`)

        Args:
            username (str)\n
            password (str)

        Returns:
            bool: status of login (`True`=Success, `False`=Failure)
        """

        # get users collection   
        users_coll_name = getenv("NEXT_PUBLIC_ROOT_USER_COLLECTION")
        users_coll_ref  = self.db.collection(users_coll_name)

        # use collection to obtain $username's reference
        user_ref = users_coll_ref.document(username)

        # check of user even exists
        user: DocumentSnapshot = user_ref.get()

        # reject if user entry doesnt exist in the database
        if not user.exists:
            return False

        user_info = user.to_dict()

        # check if passwords match
        if user_info['password'] != password:
            return False


        # save "user"'s ref for easy access later
        self.user_ref = user_ref

        return True


    def logout(self):
        """Sets the user-ref to `None`"""
        self.user_ref = None


    def set_data_for_user(self, data: Dict, with_timestamp: bool=True) -> bool:
        """Set `data` for the currently logged in user

        Args:
            data (Dict): Data to be saved to the user database
            with_timestamp (bool, optional): save with timestamp or not

        Raises:
            ValueError: if there is no logged in user currently

        Returns:
            bool: _description_
        """

        if self.user_ref is None:
            raise ValueError("User not logged in")
        
        try:
            self.user_ref.set(data, merge=True)
            self.stamp_time()
        except:
            return False

        return True



FBC = FirebaseConnection()
FBC.login('abc', 'xxxe')
FBC.set_data_for_user({'a': 15})