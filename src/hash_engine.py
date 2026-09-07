import hashlib


def generate_hash(password, algorithm="sha256"):
    """
    Generate a hash for educational comparison.
    MD5 is included only for demonstration, not secure storage.
    """
    password_bytes = password.encode("utf-8")

    if algorithm == "md5":
        return hashlib.md5(password_bytes).hexdigest()

    elif algorithm == "sha256":
        return hashlib.sha256(password_bytes).hexdigest()

    else:
        raise ValueError("Unsupported algorithm")


def main():
    print("=== Password Security Analyzer ===")

    password = input("Enter a test password: ")

    print("\nHash Results:")
    print("MD5:    ", generate_hash(password, "md5"))
    print("SHA-256:", generate_hash(password, "sha256"))


if __name__ == "__main__":
    main()
