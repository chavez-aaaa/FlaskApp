from flask_bcrypt import Bcrypt
from flask import Flask

app = Flask(__name__)
bcrypt = Bcrypt(app)

clave = "123456"
hash_clave = bcrypt.generate_password_hash(clave).decode("utf-8")
print(hash_clave)
