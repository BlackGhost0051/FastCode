import hashlib

class CryptoManager:
    def __init__(self):
        self

    def make_hash(self, password: str, salt: str = None) -> str:
        if not salt:
            salt = hashlib.sha3_512(os.urandom(32)).hexdigest()[:64]
        salted_password = salt + password
        hashed = hashlib.sha3_512(salted_password.encode()).hexdigest()
        return f"{salt}${hashed}"

    def verify_password(self, password: str, hashed_password: str) -> bool:
        try:
            salt, stored_hash = hashed_password.split('$')
            salted_password = salt + password
            computed_hash = hashlib.sha3_512(salted_password.encode()).hexdigest()
            return computed_hash == stored_hash
        except ValueError:
            raise ValueError("Invalid hashed password format")

