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
            token = jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")
            return token
        except Exception as e:
            raise ValueError(f"Error generating token: {e}")

    @staticmethod
    def get_token_info(token):
        try:
            decoded_payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            return decoded_payload
        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired"}
        except jwt.DecodeError:
            return {"error": "Token decode error"}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}
        except Exception as e:
            return {"error": f"Error getting token: {e}"}

    @staticmethod
    def verify_token(token) -> bool:
        if not token:
            return False

        if token is None:
            return False

        if "error" in JWTManager.get_token_info(token):
            return False
        return True