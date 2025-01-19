import jwt
import datetime

from config import Config


class JWTManager:
    @staticmethod
    def generate_token(user_id, username, expires_in=3600):
        try:
            payload = {
                "user_id": user_id,
                "username": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in),
                "iat": datetime.datetime.utcnow()
            }
            secret_key = Config.SECRET_KEY
            token = jwt.encode(payload, secret_key, algorithm="HS256")
            return token
        except Exception as e:
            raise ValueError(f"Error generating token: {e}")

    @staticmethod
    def verify_token(token):
        try:
            secret_key = Config.SECRET_KEY
            decoded_payload = jwt.decode(token, secret_key, algorithms=["HS256"])
            return decoded_payload
        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired"}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}