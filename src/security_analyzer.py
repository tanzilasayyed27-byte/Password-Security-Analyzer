import re
import math
import secrets
import hashlib
import string


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "welcome",
    "letmein",
    "iloveyou"
}


def analyze_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    if password.lower() in COMMON_PASSWORDS:
        return 0, "VERY WEAK"

    if score <= 2:
        return score, "WEAK"
    elif score <= 4:
        return score, "MEDIUM"
    else:
        return score, "STRONG"


def calculate_entropy(password):
    pool = 0

    if any(c.islower() for c in password):
        pool += 26

    if any(c.isupper() for c in password):
        pool += 26

    if any(c.isdigit() for c in password):
        pool += 10

    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)

    if pool == 0:
        return 0

    return round(len(password) * math.log2(pool), 2)


def generate_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


def generate_salted_hash(password):
    salt = secrets.token_hex(16)
    salted_hash = hashlib.sha256(
        (salt + password).encode()
    ).hexdigest()

    return salt, salted_hash


def main():
    print("=" * 60)
    print("       ADVANCED PASSWORD SECURITY ANALYZER")
    print("=" * 60)

    password = input("Enter a TEST password: ")

    score, strength = analyze_strength(password)
    entropy = calculate_entropy(password)
    password_hash = generate_hash(password)
    salt, salted_hash = generate_salted_hash(password)

    print("\n--- SECURITY ANALYSIS ---")
    print(f"Length              : {len(password)}")
    print(f"Security Score       : {score}/6")
    print(f"Password Strength    : {strength}")
    print(f"Entropy              : {entropy} bits")

    print("\n--- SHA-256 HASH ---")
    print(password_hash)

    print("\n--- SALTED SHA-256 ---")
    print(f"Salt                 : {salt}")
    print(f"Salted Hash          : {salted_hash}")

    print("\n--- RECOMMENDATION ---")

    if strength in ("WEAK", "VERY WEAK"):
        print("Use a longer, unique password with mixed character types.")
    elif entropy < 60:
        print("Increase password length and randomness.")
    else:
        print("Password meets the basic security requirements.")

    print("=" * 60)


if __name__ == "__main__":
    main()
