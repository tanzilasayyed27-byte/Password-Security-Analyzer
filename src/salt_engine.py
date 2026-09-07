import hashlib
import secrets


def generate_salted_hash(password):
    salt = secrets.token_hex(16)

    salted_hash = hashlib.sha256(
        (salt + password).encode()
    ).hexdigest()

    return salt, salted_hash


def verify_salted_password(password, salt, stored_hash):
    new_hash = hashlib.sha256(
        (salt + password).encode()
    ).hexdigest()

    return new_hash == stored_hash


def main():
    print("=== Secure Salted Hash Generator ===")

    password = input("Enter a test password: ")

    salt, salted_hash = generate_salted_hash(password)

    print("\nSecurity Results:")
    print(f"Salt:        {salt}")
    print(f"SHA-256:     {salted_hash}")

    verified = verify_salted_password(
        password,
        salt,
        salted_hash
    )

    print(f"\nVerification: {'SUCCESS' if verified else 'FAILED'}")


if __name__ == "__main__":
    main()
