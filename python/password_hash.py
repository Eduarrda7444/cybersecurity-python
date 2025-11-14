import hashlib
import bcrypt

type_hash = int(input("Tipos de hash:\n 1 - SHA256\n 2 - Bcrypt\n 3 - MD5\n 4 - SH1 \nDigite um número de 1 a 4: "))
password = input("Digite a senha que deseja hashear: ").encode('utf-8')

if type_hash == 1:
    # Hashing com SHA256
    hashed_password = hashlib.sha256(password).hexdigest()
    print(f"Senha hasheada (SHA256): {hashed_password}")
elif type_hash == 2:
    # Hashing com Bcrypt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    print(f"Senha hasheada (Bcrypt): {hashed_password.decode('utf-8')}")
elif type_hash == 3:
    # Hashing com MD5
    hashed_password = hashlib.md5(password).hexdigest()
    print(f"Senha hasheada (MD5): {hashed_password}")
elif type_hash == 4:
    # Hashing com SHA1
    hashed_password = hashlib.sha1(password).hexdigest()
    print(f"Senha hasheada (SHA1): {hashed_password}")
else:
    print("Tipo de hash inválido. Por favor, escolha entre 1 e 4.")