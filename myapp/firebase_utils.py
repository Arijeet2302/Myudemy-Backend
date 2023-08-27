import firebase_admin
from firebase_admin import auth, credentials


cred = credentials.Certificate("E:/Projects/myudemybackend/myudemy-32b19-firebase-adminsdk-wpiec-713fdc43ad.json")
firebase_admin.initialize_app(cred)

def create_custom_token(uid, additional_claims=None):
    return auth.create_custom_token(uid, additional_claims)

def get_user(uid):
    return auth.get_user(uid)

def verify_id_token(id_token):
    return auth.verify_id_token(id_token)
