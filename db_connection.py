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

