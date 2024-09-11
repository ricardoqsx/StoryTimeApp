import secrets

# Generar una clave secreta de 16 bytes en formato hexadecimal
secret_key = secrets.token_hex(16)
print(secret_key)