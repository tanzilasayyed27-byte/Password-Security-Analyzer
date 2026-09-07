from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


def hash_password(password):
    return ph.hash(password)


def verify_password(password, stored_hash):
    try:
        return ph.verify(stored_hash, password)
    except VerifyMismatchError:
        return False


def main():
    print("=== Argon2id Secure Password Hashing ===")

    password = input("Enter TEST password: ")

    hashed = hash_password(password)

    print("\nArgon2id Hash:")
    print(hashed)

    print("\nPassword Verification:")

    correct = verify_password(password, hashed)

    if correct:
        print("✓ Correct password: VERIFIED")
    else:
        print("✗ Password verification FAILED")

    wrong_password = "WrongTestPassword123!"
    wrong_result = verify_password(wrong_password, hashed)

    if wrong_result:
        print("✗ Security test FAILED")
    else:
        print("✓ Wrong password correctly rejected")


if __name__ == "__main__":
    main()
