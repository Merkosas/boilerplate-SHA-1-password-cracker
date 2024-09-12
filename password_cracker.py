import hashlib

def crack_sha1_hash(hash_value, use_salts=False):
    # Read the top 10,000 passwords
    with open('top-10000-passwords.txt', 'r') as file:
        passwords = [line.strip() for line in file]

    # Read the known salts
    salts = []
    if use_salts:
        with open('known-salts.txt', 'r') as file:
            salts = [line.strip() for line in file]

    # Function to hash a password
    def hash_password(password):
        return hashlib.sha1(password.encode()).hexdigest()

    # Check each password
    for password in passwords:
        if use_salts:
            # Check with each salt prepended and appended
            for salt in salts:
                if hash_password(salt + password) == hash_value:
                    return password
                if hash_password(password + salt) == hash_value:
                    return password
        else:
            # Check without salts
            if hash_password(password) == hash_value:
                return password

    return "PASSWORD NOT IN DATABASE"
