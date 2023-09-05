import jwt
import datetime
from decouple import config
from JwtAuthentication.settings import SECRET_KEY

#----------------- CREATE CUSTOM TOKEN ----------------_#

def create_access_token(id):
    payload = {
        "_id": str(id),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=43200),
        "iat": datetime.datetime.utcnow(),
    }
    return jwt.encode(payload, SECRET_KEY , algorithm='HS256')